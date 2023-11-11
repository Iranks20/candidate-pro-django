
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
    path('product-page/<int:product_id>/', views.productPage, name='productPage'),
    path('shop-cart/', views.shopCart, name='shopCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myaccount/', views.myAccount, name='myAccount'),
    path('join/', views.join, name='join'),
    path('mission/', views.mission, name='mission'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('checkout_order/', views.checkout_order, name='checkout_order'),
    path('news_details/<int:news_id>/', views.news_details, name='news_details'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
