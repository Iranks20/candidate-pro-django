
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import F
from django.db.models.functions import TruncMonth
from django.views.generic import ListView
from datetime import datetime, timedelta
from django.contrib import messages

from .models import Campaign
from .models import Priorities
from .models import priorityExamples
from .models import otherPriorities
from .models import Meet
from .models import Testimonials
from .models import Products
from .models import UserProfile
from .models import News
from .models import Event
from .models import Mission
from .models import Subscriber
from .models import CheckoutOrder
from .models import Category
from .models import NewsArchive


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
def mission(request):
    return render(request, 'mkprofile/news_single.html')
def contact(request):
    return render(request, 'mkprofile/contact.html')
def news_details(request):
    return render(request, 'mkprofile/news_details.html')
def issues_details(request):
    return render(request, 'mkprofile/issues_details.html')


# data for index.html
def index(request):
    campaigns = Campaign.objects.all()
    priorities = Priorities.objects.all()
    priorityexamples = priorityExamples.objects.all()
    meet = Meet.objects.all()
    testimonials = Testimonials.objects.all()
    products = Products.objects.all()
    latest_news = News.objects.order_by('-date').first()
    recent_events = Event.objects.order_by('-date')[:2]

    return render(request, 'mkprofile/index.html', {
    'campaigns': campaigns,
    'priorities': priorities,
    'priorityexamples': priorityexamples,
    'meet': meet,
    'testimonials': testimonials,
    'products': products,
    'latest_news': latest_news,
    'recent_events': recent_events,
    })
    # latest news
# data for issues.html
def issues(request):
    priorityexamples = priorityExamples.objects.all()
    otherpriorities = otherPriorities.objects.all()

    return render(request, 'mkprofile/issues.html', {
    'priorityexamples': priorityexamples,
    'otherpriorities': otherpriorities,
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
    categories = Category.objects.all()
    archives = NewsArchive.objects.all()
    return render(request, 'mkprofile/news_sidebar.html', {'news_entries': news_entries, 'categories': categories, 'archives': archives})

# products
def productCategory(request):
    product_categories = Products.objects.all()
    return render(request, 'mkprofile/category_page.html', {'product_categories': product_categories})

# events
def events(request):
    # Get the current date to set as the default selected month
    current_month = datetime.now().strftime("%Y-%m")

    # Convert the current month to a date object
    selected_month = datetime.strptime(current_month, '%Y-%m').date()

    # Calculate the first day of the current month
    first_day = selected_month.replace(day=1)

    # Calculate the last day of the current month
    if selected_month.month == 12:
        next_month = selected_month.replace(year=selected_month.year + 1, month=1)
    else:
        next_month = selected_month.replace(month=selected_month.month + 1)

    last_day = next_month - timedelta(days=1)

    # Retrieve events for the current month
    events = Event.objects.filter(date__range=[first_day, last_day]).order_by('date')

    # Create a list of days for the current month with associated events
    days = []
    current_day = first_day

    while current_day <= last_day:
        day_events = events.filter(date=current_day)
        days.append({'day': current_day, 'events': day_events})
        current_day += timedelta(days=1)

    # return render(request, 'mkprofile/event_month.html', {'days': days, 'selected_month': selected_month})
    return render(request, 'mkprofile/event_month.html', {'days': days, 'current_month': current_month})
    

# filtered events

def filter_events(request):
    selected_month_str = request.POST.get('selected_month')

    if selected_month_str:
        selected_month = datetime.strptime(selected_month_str, '%Y-%m').date()

        # Calculate the first day of the month
        first_day = selected_month.replace(day=1)

        # Calculate the last day of the month
        if selected_month.month == 12:
            next_month = selected_month.replace(year=selected_month.year + 1, month=1)
        else:
            next_month = selected_month.replace(month=selected_month.month + 1)

        last_day = next_month - timedelta(days=1)

        # Retrieve events for the selected month
        events = Event.objects.filter(date__month=selected_month.month, date__year=selected_month.year)

        # Create a list of days for the selected month with associated events
        days = []
        current_day = first_day

        while current_day <= last_day:
            day_events = events.filter(date=current_day)
            days.append({'day': current_day, 'events': day_events})
            current_day += timedelta(days=1)

        return render(request, 'mkprofile/event_month.html', {'days': days, 'selected_month': selected_month})

    else:
        return redirect('events')

# mission
def mission(request):
    missions = Mission.objects.all()
    
    return render(request, 'mkprofile/news_single.html', {'missions': missions})

# subscribe
from django.http import JsonResponse

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['newsletter-email']
        try:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                message = 'You have subscribed successfully!'
                response_data = {'success': True, 'message': message}
            else:
                message = 'Email address already subscribed.'
                response_data = {'success': False, 'message': message}
        except Exception as e:
            message = 'An error occurred: ' + str(e)
            response_data = {'success': False, 'message': message}

        return JsonResponse(response_data)

    return render(request, 'get_involved.html')

#product details
def productPage(request, product_id):
    product_details = get_object_or_404(Products, pk=product_id)
    return render(request, 'mkprofile/product_page.html', {'product_details': product_details})

#news details
def news_details(request, news_id):
    news_details = get_object_or_404(News, pk=news_id)
    categories = Category.objects.all()
    archives = NewsArchive.objects.all()
    return render(request, 'mkprofile/news_detail.html', {'news_details': news_details, 'categories': categories, 'archives': archives})

# issues details
def issues_details(request, issues_id):
    issues_details = get_object_or_404(priorityExamples, pk=issues_id)
    return render(request, 'mkprofile/issues_details.html', {'issues_details': issues_details})

# product checkout details
def checkout(request):
    product_id = request.GET.get('product_id')
    size = request.GET.get('size')
    quantity = request.GET.get('quantity')
    product_details = get_object_or_404(Products, pk=product_id)
    quantity = int(quantity)
    product_price = float(product_details.product_price)
    total = product_price * quantity

    return render(request, 'mkprofile/checkout.html', {'product_id': product_id, 'quantity': quantity, 'product_details': product_details, 'total': total, 'size': size})

def checkout_order(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        town_city = request.POST.get('town_city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        order_notes = request.POST.get('order_notes')
        product_name = request.POST.get('product_name')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
        unit_cost = request.POST.get('unit_cost')
        delivery_cost = request.POST.get('delivery_cost')
        total_cost = request.POST.get('total_cost')

        # Save data to CheckoutOrder model
        checkout_order = CheckoutOrder(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            address=address,
            town_city=town_city,
            phone=phone,
            email=email,
            order_notes=order_notes,
            product_name=product_name,
            size=size,
            quantity=quantity,
            unit_cost=unit_cost,
            delivery_cost=delivery_cost,
            total_cost=total_cost
        )
        checkout_order.save()

        messages.success(request, 'Order placed successfully!')
        return redirect('https://flutterwave.com/pay/hpimxsvovffx') 

    return render(request, 'mkprofile/checkout.html')

#news categories
def news_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    categories = Category.objects.all()
    archives = NewsArchive.objects.all()
    news_list = category.news.all()
    return render(request, 'mkprofile/news_by_category.html', {'category': category, 'news_list': news_list, 'categories': categories, 'archives': archives})

def news_by_year(request, year):
    archive = get_object_or_404(NewsArchive, year=year)
    news_list = archive.news.all()
    archives = NewsArchive.objects.all()
    categories = Category.objects.all()
    return render(request, 'mkprofile/news_by_year.html', {'archive': archive, 'news_list': news_list, 'archives': archives, 'categories': categories})
    


