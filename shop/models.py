from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name= models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default= "")
    price = models.IntegerField(default=0)
    desc= models.CharField(max_length=500)
    userratings=models.CharField(max_length=10, default="")
    onlineratings=models.FloatField(default="")
    pub_date =models.DateField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
   
    def __str__(self):
        return self.product_name


#contact db
class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default= "")
    desc= models.CharField(max_length=500, default= "")
 

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=30)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10]+"...."


class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE   )
    post=models.ForeignKey(Product, on_delete=models.CASCADE   )
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField( default=now)

    def __str__(self):
        return self.comment[0:15] + "..." + " by " + self.user.username