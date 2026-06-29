from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here. 

# class UserProfile(models.Model):
#     ROLE_CHOICES = (
#         ("Customer", "Customer"),
#         ("Waiter", "Waiter"),
#         ("Chef", "Chef"),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES) 

#     def __str__(self):
#         return self.user.username
    
class Food(models.Model):
    CATEGORY_CHOICES = [
        ('Starter', 'Starter'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Beverage', 'Beverage'),
    ]
    MEAL_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Night', 'Night'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    meal_time = models.CharField(max_length=20,choices=MEAL_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='food_images/') 
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RestaurantTable(models.Model):
    table_no = models.IntegerField(unique=True)
    seats = models.IntegerField()
    STATUS = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
    )
    status = models.CharField(max_length=20,choices=STATUS,default='Available')

    def __str__(self):
        return f"Table {self.table_no}"

class Cart(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    table = models.ForeignKey(RestaurantTable,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.customer.username} - {self.food.name}"
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    table= models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'pending'),
        ('Confirmed', 'Confirmed'),
        ('preparing', 'preparing'),
        ('Ready', 'Ready'),
        ("Bill Generated", "Bill Generated"),
        ('Completed', 'Completed')], default='Pending')
    total_amt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    @property
    def total_price(self):
        return self.price * self.quantity 

    
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200, blank=True, default=" ")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name