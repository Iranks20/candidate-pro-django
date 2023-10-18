
from django.shortcuts import render
from .models import Campaign
from .models import Priorities
from .models import priorityExamples
from .models import Meet
from .models import Testimonials
from .models import Products

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
    priorities = Priorities.objects.all()
    priorityexamples = priorityExamples.objects.all()
    meet = Meet.objects.all()
    testimonials = Testimonials.objects.all()
    products = Products.objects.all()

    return render(request, 'mkprofile/index.html', {
    'campaigns': campaigns,
    'priorities': priorities,
    'priorityexamples': priorityexamples,
    'meet': meet,
    'testimonials': testimonials,
    'products': products
    })

# data for issues.html
def issues(request):
    priorityexamples = priorityExamples.objects.all()

    return render(request, 'mkprofile/issues.html', {
    'priorityexamples': priorityexamples,
    })