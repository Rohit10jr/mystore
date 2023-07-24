from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Product, Contact, Orders, OrderUpdate, BlogComment
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from shop.templatetags import extras

# Create your views here.
def index(request):
 
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods} 
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params={'allprods': allprods}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower() or query in item.subcategory.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
        # return redirect('shophome')
    return render(request, 'shop/search.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        # print(name, email, phone, desc)
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html', {'thank':thank})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address1', '') +" "+ request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')

        order=Orders(items_json=items_json,name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your order has been placed successfully")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id':id})
    return render(request, 'shop/checkout.html')

def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderId','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(order_id=orderid, email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time': item.timestamp })
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                 return HttpResponse('{"status":"No item"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    
    return render(request, 'shop/tracker.html')

def productview(request, myid):
    #fetch the product id
    product = Product.objects.filter(id=myid).first()
    comments= BlogComment.objects.filter(post=product, parent=None)
    replies= BlogComment.objects.filter(post=product).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'comments': comments, 'user': request.user, 'product':product, 'replyDict': replyDict}
   
    return render(request, 'shop/prodview.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        postname=request.POST.get('postname')
        postid=request.POST.get('postno')
        user=request.user
        # id_ = request.GET.get('id')
        # postno =request.POST.get('postno')
        product= Product.objects.get(product_name=postname)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=product)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")      
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=product , parent=parent)
            postid=request.POST.get('postno')
            comment.save()
            messages.success(request, "Your reply has been posted successfully")  
    return redirect(f"/shop/products/{postid}")

# user login and signup
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
   # check for errorneous input
        if len(username)>25:
            messages.error(request, " Your user name must be under 25 characters")
            return redirect('shophome')
        # check for alphanumeric
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('shophome')
        #check for password missmatch
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('shophome')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('shophome')

    else:
        return HttpResponse("404 - Not found")
    
def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("shophome")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("shophome")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('shophome')


@csrf_exempt
def handlerequest(request):
    pass