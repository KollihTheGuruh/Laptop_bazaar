from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from mainapp.forms.registration_form import RegistrationForm
from .models import Laptop, User, Order
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
def compare_view(request):
    # This will depend on how you're planning to implement the comparison feature.
    # For instance, you might use query parameters to get the IDs of laptops to compare.
    return render(request, 'compare.html')

# Checkout View
def checkout_view(request):
    if request.method == "POST":
        # Process the checkout form
        # Create an order instance, etc.
        return redirect('payment')
    else:
        # Display checkout form
        return render(request, 'checkout.html')

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

    # Render a template with the laptop details
    return render(request, 'laptop_detail.html', {'laptop': laptop})