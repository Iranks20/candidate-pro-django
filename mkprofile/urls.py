
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('issues/', views.issues, name='issues'),
    path('events/', views.events, name='events'),
    path('product-category/', views.productCategory, name='productCategory'),
    path('product-page/', views.productPage, name='productPage'),
    path('shop-cart/', views.shopCart, name='shopCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myaccount/', views.myAccount, name='myAccount'),
    path('join/', views.join, name='join'),
    path('contact/', views.contact, name='contact'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
