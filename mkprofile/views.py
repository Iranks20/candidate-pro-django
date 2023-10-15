
from django.shortcuts import render
from .models import Campaign

def index(request):
    return render(request, 'mkprofile/index.html')
def news(request):
    return render(request, 'mkprofile/news_sidebar.html')
def issues(request):
    return render(request, 'mkprofile/issues.html')
def events(request):
    return render(request, 'mkprofile/event_month.html')
def productCategory(request):
    return render(request, 'mkprofile/category_page.html')
def productPage(request):
    return render(request, 'mkprofile/product_page.html')
def shopCart(request):
    return render(request, 'mkprofile/shop_cart.html')
def checkout(request):
    return render(request, 'mkprofile/checkout.html')
def myAccount(request):
    return render(request, 'mkprofile/my_account.html')
def join(request):
    return render(request, 'mkprofile/get_involved.html')
def contact(request):
    return render(request, 'mkprofile/contact.html')

# data for index.html
def index(request):
    campaigns = Campaign.objects.all()
    return render(request, 'mkprofile/index.html', {'campaigns': campaigns})