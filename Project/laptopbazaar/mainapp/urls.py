from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('products/', views.product_view, name='product_view'),
    path('compare/', views.compare_view, name='compare_view'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('payment/', views.payment_view, name='payment_view'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('laptop_detail/<int:laptop_id>/', views.laptop_detail, name='laptop_detail'),
    # Add other URL patterns as needed
]
