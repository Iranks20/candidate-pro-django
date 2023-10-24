
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Campaign
from .models import Priorities
from .models import priorityExamples
from .models import Meet
from .models import Testimonials
from .models import Products
from .models import UserProfile
from django.views.generic import ListView
from .models import News


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

# registering joining user
def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code')
        
        # Collect all checked checkboxes
        checked_boxes = []
        for i in range(1, 7):
            checkbox_name = f'checkbox-{i}'
            if checkbox_name in request.POST:
                checked_boxes.append(request.POST[checkbox_name])
        
        # Join the checked checkboxes with a separator (e.g., comma)
        checkboxes = ', '.join(checked_boxes)
        
        comments = request.POST.get('comments', '')

        # Create a new UserProfile object and save it to the database
        UserProfile.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            zip_code=zip_code,
            checkboxes=checkboxes,
            comments=comments
        )

        # You can redirect to a success page or simply redirect back to the 'join' page
        return redirect('join')

    return render(request, 'join.html')

# news
def news(request):
    news_entries = News.objects.all()
    return render(request, 'mkprofile/news_sidebar.html', {'news_entries': news_entries})

# products
def productCategory(request):
    product_categories = Products.objects.all()
    return render(request, 'mkprofile/category_page.html', {'product_categories': product_categories})
