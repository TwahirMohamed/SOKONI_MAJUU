# 🔹 High-Level Architecture
# 1.  Frontend (UI):

Django templates (or a React/Vue frontend consuming Django REST API).

## The user shall be all to:

    1. Search for products (via Amazon / other store APIs).

    2. View product details (price, images, description).

    3. Add items to cart.

    4. Checkout + pay.

# 2.  Backend (Django):

* Product Search & Display

    Integrate APIs (Amazon Product Advertising API, eBay API, Walmart API, etc).

* Cart & Checkout

    Standard e-commerce flow (Django models for Cart, Order, Payment).

* Payment Gateway

    Stripe, PayPal, Flutterwave, or similar.

* Fulfillment Workflow

    a. Once the user pays, the system places an order with the online store’s API using your account.

    b. The item is shipped to your local warehouse (your address).

    c. Then the order is re-ship internationally.

# 3. Database (PostgreSQL/MySQL)

* Users

* Products (cached from APIs for display)

* Orders

* Payments

* Shipments / Tracking

# 🛠️ Django App Breakdown
* users → Authentication, profiles, addresses.

* catalog → Product search, product detail views.

* cart → Shopping cart functionality.

* orders → Order models, status tracking.

* payments → Stripe/PayPal integration.

* shipping → Warehouse receipt, international delivery.

* core → Shared utils, templates, homepage.

# ⛓️ API Integrations
* Amazon Product Advertising API
Lets you search products, get details, and affiliate links.
⚠️ Requires approval from Amazon + affiliate setup.

## Alternative sources:

* eBay API (simpler than Amazon’s).

* Walmart API.

* AliExpress Open Platform.

* Or a scraping API (ScraperAPI, BrightData) → not as reliable/allowed.

# ⛓️ Order Flow
* Step 1: User searches product
→ Django calls Amazon/eBay API → show results.

* Step 2: User adds to cart & checks out
→ Pay via Stripe/PayPal inside your app.

* Step 3:The app  places order.

Using  our account & API.

* Step 4: Ship to the warehouse/local address.

* Step 5: Item arrives at warehouse

* Item marked  as "received".

* Step 6:  Generate new shipping (DHL, FedEx, Aramex, etc) to the user’s international address.

Tracking & Delivery

Your app updates order status + provides tracking.

# Database entities

# users/models.py
```text
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.TextField()
```

# catalog/models.py
```text

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    external_id = models.CharField(max_length=100)  # ID from Amazon/eBay API
    source = models.CharField(max_length=50)  # amazon, ebay, etc.
```
# orders/models.py
```text
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending Payment'),
        ('paid', 'Paid'),
        ('ordered', 'Ordered from Supplier'),
        ('received', 'Received at Warehouse'),
        ('shipped', 'Shipped Internationally'),
        ('delivered', 'Delivered'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
```

# payments/models.py
```text
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('initiated', 'Initiated'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ])
    transaction_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```
#  💵 Payment Gateway Setup
1. Stripe Checkout (easiest to integrate with Django):
import stripe
from django.conf import settings
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY

```text
def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': order.product.title,
                },
                'unit_amount': int(order.product.price * 100),
            },
            'quantity': order.quantity,
        }],
        mode='payment',
        success_url='https://yourapp.com/success/',
        cancel_url='https://yourapp.com/cancel/',
    )
    return redirect(session.url, code=303)
```

2. MPESA 

# Each app and its features:
## User App
1. manages user registrations.
2. manages login, logout and authentications
