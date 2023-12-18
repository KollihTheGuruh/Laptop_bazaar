from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from mainapp.forms.registration_form import RegistrationForm
from .models import Laptop, LaptopModel, User, Order, CartItem
from django.http import HttpResponse
# Add any other necessary imports

def home_view(request):
    # Add your view logic here
    return render(request, 'index.html')

def about_us_view(request):
    # Your view logic here
    return render(request, 'about_us.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Log in the user
            login(request, user)
            
            # Redirect to a success page or home page
            return redirect('home')  # Change 'home' to the name of your home page URL pattern
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

# Dashboard View
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Additional logic based on user type (superuser, client, customer)
    return render(request, 'dashboard.html')

# Product View
def product_view(request):
    laptops = Laptop.objects.all()
    return render(request, 'product_list.html', {'laptops': laptops})

# Compare View
def fetch_laptops_by_ids(laptop_ids):
    """
    Fetch laptops by their IDs.

    Args:
    - laptop_ids: List of laptop IDs.

    Returns:
    - List of laptop instances.
    """
    return Laptop.objects.filter(id__in=laptop_ids)

def compare_view(request):
    # Get laptop IDs from the query parameters
    laptop_ids = request.GET.get('laptop_ids', '').split(',')

    # Filter out empty strings from the split result
    laptop_ids = list(filter(lambda x: x.strip(), laptop_ids))

    # Fetch laptops using the IDs
    laptops = fetch_laptops_by_ids(laptop_ids)

    # Render the compare view template
    return render(request, 'compare_view.html', {'laptops': laptops})
# Checkout View
def checkout_view(request):
    if request.method == "POST":
        # Process the checkout form
        # Create an order instance, etc.
        return redirect('payment')
    else:
        # Display checkout form
        return render(request, 'checkout.html')
    
def contact_us_view(request):
    
        return render(request, 'contact_us.html')

# Payment View
def payment_view(request):
    if request.method == "POST":
        # Process payment here
        # Integrate with M-Pesa or other payment gateways
        return redirect('success')
    else:
        return render(request, 'payment.html')
    
def laptop_detail(request, laptop_id):
    # Retrieve the laptop object from the database using the laptop_id
    laptop = get_object_or_404(Laptop, id=laptop_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        # Check if the item is already in the cart
        cart_item, created = CartItem.objects.get_or_create(
            laptop=laptop,
            user=request.user  # Assuming you have user authentication
        )

        # If the item is already in the cart, update the quantity
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        # If the item is not in the cart, create a new cart item
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return redirect('cart_view')

    # Render a template with the laptop details
    return render(request, 'laptop_detail.html', {'laptop': laptop})

def cart_view(request):
    # Retrieve cart items from the database or wherever they are stored
    cart_items = CartItem.objects.all()  # Modify this query based on your model structure and logic
    
    return render(request, 'cart_view.html', context={'cart_items': cart_items})
