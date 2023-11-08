# E-Commerce Project with Django

![Django](https://img.shields.io/badge/Django-3.x-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-red)

Welcome to my E-Commerce Project, a feature-rich, customizable Django-based online shopping platform. This project empowers you to build and launch your e-commerce store with ease.

![E-Commerce Project Screenshot](/screenshot.png)

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Configuration](#configuration)
3. [Usage](#usage)
   - [Admin Panel](#admin-panel)
4. [Contributions](#contributions)
5. [Acknowledgments](#acknowledgments)

## Features

- **Product Management:** Easily add, update, and delete products with images, descriptions, and prices.
- **User Authentication:** Secure registration, login, and profile management for customers.
- **Shopping Cart:** Add and manage items in a shopping cart before checkout.
- **Order Processing:** Manage orders, shipping, and order history.
- **Admin Dashboard:** Convenient admin panel for product, order, and customer management.
- **Search and Filters:** Quickly find products with search and filter options.
- **Responsive Design:** A mobile-friendly interface for users on all devices.

## Getting Started

Follow these steps to get your Django E-Commerce Project up and running:

### Installation

1. Clone the repository:
```
git clone https://github.com/Rohit10jr/Ecommerce-site.git
```  
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
3. Install the project dependencies:
```
pip install -r requirements.txt
```
4. Apply database migrations:
```
python manage.py migrate
```
5. Create a superuser account for admin access:
```
 python manage.py createsuperuser
````
6. Start the development server:
```
python manage.py runserver
```
7.Access the project at http://localhost:8000 and the admin panel at http://localhost:8000/admin.

## Configuration

Customize your project settings by modifying the /settings.py file. This includes database settings, payment gateway configurations, and more.

## Usage

-Log in as a superuser to access the admin panel and add products to the store.
-As a regular user, explore the website, add items to your cart, and proceed to checkout.
-Manage your orders, view order history, and complete transactions.

## Admin Panel

Use the admin panel at http://localhost:8000/admin to manage products, categories, orders, and customer accounts with ease.

##Customization

Customize your e-commerce store by adding categories, configuring payment options, and fine-tuning the project settings via the admin panel.

## Contributions

Contributions to the Awesome E-Commerce Project are highly encouraged. To contribute, please follow these guidelines:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Submit a pull request with a detailed description of your changes.

## Acknowledgments

This project was developed with Django and relies on various open-source libraries. Thanks to the Django community and contributors behind these tools.

