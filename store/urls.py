from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.login import Login, logout
from .views.checkout import CheckOut
from .views.cart import Cart
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from .views.Signup import Signup
from .views.home import home


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home', home, name='home'),
    path('store', store, name='store'),
    path('Signup', Signup.as_view(), name='Signup'),
    path('Login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
