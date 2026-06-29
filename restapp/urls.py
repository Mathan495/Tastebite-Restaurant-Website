from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.about_page, name="about"),
    path('menu/', views.menu_page, name="menu"),
    path("add-to-cart/<int:food_id>/", views.add_to_cart, name="add_to_cart"),
    path("select-table/<int:table_id>/", views.select_table, name="select_table"),
    path("order-cart/", views.order_cart, name="order_cart"),
    path("remove-cart-item/<int:item_id>/", views.remove_cart_item, name="remove_cart_item"),
    path("place-order/", views.place_order, name="place_order"),
    path("order-success/", views.order_successpage, name="order_success"),
    path('contact/', views.contact_page, name="contact"),
    path("waiter-dashboard/",views.waiter_dashboard, name="waiter_dashboard"),
    path("confirm-order/<int:order_id>/", views.confirm_order, name="confirm_order"),
    path('chef/',views.chef_page,name='chef'),
    path("start-preparing/<int:order_id>/", views.start_preparing, name="start_preparing"),
    path("mark-ready/<int:order_id>/", views.mark_ready, name="mark_ready"),
    path("serve-order/<int:order_id>/", views.serve_order, name="serve_order"),
    path("generate-bill/<int:order_id>/", views.generate_bill, name="generate_bill"),
    # path("finish-order/<int:order_id>/", views.finish_order, name="finish_order"),
]
