from django.contrib import admin
from django.urls import include, path
from orders.apiviews import OrdersList,OrderDetails,CartsList,CartDetails
from core.apiviews import UsersList,UserDetails
from items.apiviews import ProductsList,ProductDetails
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UsersList.as_view(), name="Users List"),
    path('users/<int:pk>', UserDetails.as_view(), name="User Details"),
    path('orders/', OrdersList.as_view(), name="Orders List"),
    path('order/<int:pk>', OrderDetails.as_view(), name="Order Details"),
    path('products/', ProductsList.as_view(), name="Products List"),
    path('product/<int:pk>', ProductDetails.as_view(), name="Product Details"),
    path('carts/', CartsList.as_view(), name="Carts List"),
    path('cart/<int:pk>', CartDetails.as_view(), name="Cart Details"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]