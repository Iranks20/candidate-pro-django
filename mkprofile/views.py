
from django.shortcuts import render
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
from .models import Meet
from .models import Testimonials
from .models import Products
from .models import UserProfile
from .models import News
from .models import Event
from .models import Mission
from .models import Subscriber



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
def subscribe(request):
    if request.method == 'POST':
        email = request.POST['newsletter-email']
        try:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'You have subscribed successfully!')
            else:
                messages.error(request, 'Email address already subscribed.')
        except Exception as e:
            messages.error(request, 'An error occurred: ' + str(e))
        return redirect('join')
    return render(request, 'get_involved.html')