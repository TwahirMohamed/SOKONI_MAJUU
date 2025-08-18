
```text
shopmajuu/
│── manage.py
│── requirements.txt
│── README.md
│
├── shopmajuu/              # Main project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── catalog/                  # Products & APIs
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Product model (dummy first, API later)
│   ├── views.py              # Product list & detail
│   ├── urls.py
│   ├── forms.py              # (if needed for search/filtering)
│   ├── templates/
│   │   └── catalog/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       └── search_results.html
│   └── static/catalog/       # CSS/JS/images specific to catalog
│
├── orders/                   # Orders & cart
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Order model
│   ├── views.py              # Cart, checkout
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   └── orders/
│   │       ├── order_summary.html
│   │       └── order_list.html
│   └── static/orders/
│
├── payments/                 # Payment handling (Stripe, PayPal)
│   ├── __init__.py
│   ├── models.py             # Payment transactions
│   ├── views.py              # Payment flow
│   ├── urls.py
│   ├── templates/
│   │   └── payments/
│   │       └── checkout.html
│   └── static/payments/
│
├── users/                    # Authentication & profiles
│   ├── __init__.py
│   ├── models.py             # Extend User with profile info
│   ├── forms.py              # Registration/Login/Profile update
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── users/
│   │       ├── register.html
│   │       ├── login.html
│   │       └── profile.html
│   └── static/users/
│
├── warehouse/                # Shipping & local warehouse mgmt
│   ├── __init__.py
│   ├── models.py             # Warehouse, shipment tracking
│   ├── views.py              # Order tracking
│   ├── urls.py
│   ├── templates/
│   │   └── warehouse/
│   │       └── tracking.html
│   └── static/warehouse/
│
├── core/                     # Shared utilities
│   ├── __init__.py
│   ├── utils.py              # Helper functions
│   ├── mixins.py             # Shared CBV mixins
│   ├── services/             # External API integrations
│   │   ├── amazon_api.py
│   │   ├── ebay_api.py
│   │   └── payment_gateway.py
│   └── templates/core/       # Common layouts
│       ├── base.html
│       └── navbar.html
│
├── static/                   # Global static files
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/                # Global templates
    ├── base.html             # Global layout
    └── includes/             # Navbar, footer, etc.
```