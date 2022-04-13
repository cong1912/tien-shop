from django.urls import path
from mysite.controllers import page_controllers

urlpatterns = [
  path('', page_controllers.home, name='home'),
  path('about-us', page_controllers.aboutus, name='aboutus'),
  path('blog-standard', page_controllers.blogStandard, name='blog-standard'),
  path('portfolio', page_controllers.portfolio, name='portfolio'),
  path('contact', page_controllers.contact, name='contact'),
  path('product-list', page_controllers.productsList, name='product-list'),
  path('product-detail', page_controllers.productDetail, name='product-detail'),
  path('shop-account', page_controllers.account, name='shop-account'),
  path('shop-lost-password', page_controllers.lostPassword, name='lost-password'),
  path('shop-cart', page_controllers.cart, name='shop-cart'),
  path('shop-order-tracking', page_controllers.orderTracking, name='shop-order-tracking'),
  path('shop-wishlist', page_controllers.wishlist, name='shop-wishlist'),
]