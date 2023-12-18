"""
URL configuration for laptopbazaar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, include  # Import the include function
from mainapp.views import cart_view, home_view
from django.contrib.auth.views import LogoutView
from django.urls import path
from mainapp.views import about_us_view
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('mainapp.urls')),  # Include URLs from mainapp
   # path('', home_view, name='home'),  # Define the root URL pattern
    path('', home_view, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about_us/', about_us_view, name='about_us'),
    path('compare.html/', views.compare_view, name='compare_view'),
    path('contact_us.html/', views.contact_us_view, name='contact_us'),
    path('cart/', cart_view, name='cart_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
