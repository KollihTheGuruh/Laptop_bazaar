from django.urls import path
from . import views
from .views import cart_view, laptop_detail, update_cart 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('products/', views.product_view, name='product_view'),
    path('compare/', views.compare_view, name='compare_view'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('payment/', views.payment_view, name='payment_view'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('laptop_detail/<int:laptop_id>/', views.laptop_detail, name='laptop_detail'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.home_view, name='home'),
    path('contact_us/', views.contact_us_view, name='contact_us_view'),
    path('cart/', cart_view, name='cart_view'),
    path('laptop_detail/<int:laptop_id>/', laptop_detail, name='laptop_detail'),
    path('update_cart/', update_cart, name='update_cart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
