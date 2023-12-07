from django.db import models
from django.contrib.auth.models import AbstractUser

# User Models
class User(AbstractUser):
    # Extend this class with additional fields if needed
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_group_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permission_set",
        related_query_name="custom_user",
    )
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class LaptopModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Laptop Model
class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    processor = models.CharField(max_length=100)
    graphics_card = models.CharField(max_length=100)
    ram = models.IntegerField()
    storage = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    battery_life = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    ports = models.TextField()
    wireless_connectivity = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=100)
    touchpad = models.CharField(max_length=100)
    webcam = models.CharField(max_length=100)
    audio = models.CharField(max_length=100)
    build_material = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    dimensions = models.CharField(max_length=100)
    cooling_system = models.CharField(max_length=100)
    security_features = models.TextField()
    optical_drive = models.CharField(max_length=100, null=True, blank=True)
    color_options = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100)
    images = models.ImageField(upload_to='laptop_images/', null=True, blank=True, verbose_name='Laptop Image')
    def __str__(self):
        return f"{self.brand} Laptop - Price: ${self.price}, Processor: {self.processor}, Graphics Card: {self.graphics_card}, RAM: {self.ram}GB, Storage: {self.storage}, Display: {self.display}, Battery Life: {self.battery_life}, Operating System: {self.operating_system}"

# Order Model
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending', verbose_name='Order Status')

    def __str__(self):
        return f'Order {self.id} by {self.customer}'
