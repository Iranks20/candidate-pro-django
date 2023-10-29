
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('issues/', views.issues, name='issues'),
    path('events/', views.events, name='events'),
    path('filter_events/', views.filter_events, name='filter_events'),
    path('product-category/', views.productCategory, name='productCategory'),
    path('product-page/', views.productPage, name='productPage'),
    path('shop-cart/', views.shopCart, name='shopCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myaccount/', views.myAccount, name='myAccount'),
    path('join/', views.join, name='join'),
    path('mission/', views.mission, name='mission'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
