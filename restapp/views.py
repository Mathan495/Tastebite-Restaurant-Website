from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Food, ContactMessage, RestaurantTable, Cart, Order, OrderItem
from decimal import Decimal

# Create your views here.
def home(request):
    if request.session.get("role") != "Customer":
        return redirect("login")
    tables = RestaurantTable.objects.all()
    feature_foods= Food.objects.filter(price__gt = 100, is_available=True)[:6]
    return render(request, 'home.html', {"tables": tables, "featured_foods": feature_foods})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully")
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get("role")
        request.session["role"] = role

        user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, "Logged in Successfully")
        #     return redirect('home')
        if user is not None:
            login(request, user)
            if role == "Customer":
                return redirect("home")

            elif role == "Waiter":
                return redirect("waiter_dashboard")

            elif role == "Chef":
                return redirect("chef")
            else:
                messages.error(request, "Please select a valid role.")
                return redirect("login")
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
        
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request,"Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect("register")
        
        User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name) 
        messages.success(request,"Account created successfully")
        return redirect("login")
    return render(request, "register.html")

def about_page(request):
    return render(request, 'about.html')

def menu_page(request):
    foods = Food.objects.all()
    morning_foods = Food.objects.filter(meal_time="Morning")
    afternoon_foods = Food.objects.filter(meal_time="Afternoon")
    night_foods = Food.objects.filter(meal_time="Night")
    context = {
        "foods": foods,
        "morning_foods": morning_foods,
        "afternoon_foods": afternoon_foods,
        "night_foods": night_foods
    }
    return render(request,"menu.html",context)

def contact_page(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            full_name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )
        return redirect("home")
    return render(request, "contact.html")

def select_table(request, table_id):
    table = get_object_or_404(RestaurantTable, id=table_id)
    if table.status == "Booked":
        messages.error(request, "This table is already booked.")
        return redirect("home")
    table.status = "Booked"
    table.save()
    request.session["table_id"] = table.id
    return redirect("menu") 

def add_to_cart(request, food_id):
    if request.method == "POST":
        food = get_object_or_404(Food, id=food_id)
        quantity = int(request.POST.get("quantity"))
        table_id = request.session.get("table_id")
        table = get_object_or_404(RestaurantTable, id=table_id)
        Cart.objects.create(customer=request.user,table=table,food=food,quantity=quantity)
    return redirect("order_cart") 

def order_cart(request):
    cart_items = Cart.objects.filter(customer=request.user)
    total = 0
    for item in cart_items:
        total += item.food.price * item.quantity
    return render(request,"order_cart.html",{"cart_items": cart_items,"total": total,})

def remove_cart_item(request, item_id):
    item = get_object_or_404(Cart, id=item_id, customer=request.user)
    item.delete()
    return redirect("order_cart") 

def place_order(request):
    cart_items = Cart.objects.filter(customer=request.user)
    if not cart_items.exists():
        return redirect("order_cart")
    table = cart_items.first().table
    # table.status = "Booked"
    # table.save() 
    order = Order.objects.create(customer=request.user,table=table,status="pending",total_amt=0)
    total = 0
    for item in cart_items:
        OrderItem.objects.create(order=order,food=item.food,quantity=item.quantity,price=item.food.price)
        total += item.food.price * item.quantity
    order.total_amt = total
    order.save() 
    cart_items.delete()
    messages.success(request, "Order can be Successfully Created")
    # return redirect("waiter_dashboard")
    return redirect("order_success")

def order_successpage(request):
    latest_order = Order.objects.filter(customer=request.user).order_by("-id").first()
    return render(request, "order_success.html", {
        "order": latest_order
    })

def waiter_dashboard(request):
    # orders = Order.objects.all().order_by("-id")
    if request.session.get("role") != "Waiter":
        return redirect("login")
    orders = Order.objects.exclude(status="Bill Generated").order_by("-id")
    pending_count = Order.objects.filter(status="pending").count()
    confirmed_count = Order.objects.filter(status="Confirmed").count()
    preparing_count = Order.objects.filter(status="Preparing").count()
    ready_count = Order.objects.filter(status="Ready").count()
    completed_count = Order.objects.filter(status="Completed").count()
    return render(request,"waiter_dashboard.html",{"orders": orders, "pending_count": pending_count,"confirmed_count": confirmed_count,
        "preparing_count": preparing_count, "ready_count": ready_count,"completed_count": completed_count })

def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "Confirmed"
    order.save()
    return redirect("chef")

def chef_page(request):
    if request.session.get("role") != "Chef":
        return redirect("login")
    orders = Order.objects.filter(
        status__in=["Confirmed", "Preparing", "Ready"]).order_by("-id")
    context = {
        "orders": orders,
        "total_orders": Order.objects.count(),
        "confirmed_orders": Order.objects.filter(status="Confirmed").count(),
        "preparing_orders": Order.objects.filter(status="Preparing").count(),
        "ready_orders": Order.objects.filter(status="Ready").count(),
    }
    return  render(request, 'chef/chef.html', context)

def start_preparing(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "Preparing"
    order.save()
    return redirect("chef") 

def mark_ready(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "Ready"
    order.save()
    return redirect("chef")

def serve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "Completed"
    order.save()
    return redirect("waiter_dashboard")

def generate_bill(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.orderitem_set.all()

    order.status = "Bill Generated"
    order.save()

    table = order.table
    table.status = "Available"
    table.save()

    subtotal = Decimal("0.00")
    for item in order_items:
        subtotal += item.price * item.quantity
    gst = subtotal * Decimal("0.05")
    grand_total = subtotal + gst
    context = {
        "order": order,
        "order_items": order_items,
        "subtotal": subtotal,
        "gst": gst,
        "grand_total": grand_total,
    }
    return render(request, "bill.html", context)

# def finish_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     # Delete related order items first
#     order.orderitem_set.all().delete()
#     # Delete the order
#     order.delete()
#     return redirect("waiter_dashboard") 