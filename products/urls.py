from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("signup",views.signup,name="signup"),
    path('products/<product_brand>/<product_slug>',views.product_page, name='product_page'),
    path('allproducts', views.catlog ,name='allproducts')
]