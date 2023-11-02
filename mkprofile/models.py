from django.db import models

# home page heading including background image
class Campaign(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.TextField()
    background_image = models.ImageField(upload_to='campaign_backgrounds/', null=True)

    def __str__(self):
        return self.title

# mk's priorities
class Priorities(models.Model):
    title = models.CharField(max_length=100)
    title_description = models.TextField(null=True)
    def __str__(self):
        return self.title
    
# priority examples and issues
class priorityExamples(models.Model):
    priorities_heading = models.TextField()
    priorities_description = models.TextField()
    priorities_image = models.ImageField(upload_to='priorities_images/', null=True)

    def __str__(self):
        return self.priorities_heading
    
# meet mk
class Meet(models.Model):
    meet_name = models.TextField()
    meet_description = models.TextField()
    meet_image = models.ImageField(upload_to='meet_images/', null=True)

    def __str__(self):
        return self.meet_name

# testimonials why we support mk
class Testimonials(models.Model):
    testimonial_name = models.CharField(max_length=200, null=True)
    testimonial_description = models.TextField()
    testimonial_residence = models.CharField(max_length=200, null=True)
    testimonial_image = models.ImageField(upload_to='testimonial_images/', null=True)

    def __str__(self):
        return self.testimonial_name

# products
class Products(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_price = models.CharField(max_length=200, null=True)
    product_image = models.ImageField(upload_to='products_images/', null=True)

    def __str__(self):
        return self.product_name

# registering a user joining
class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10)
    checkboxes = models.CharField(max_length=255, null=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# news
class News(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    iframe = models.URLField(blank=True, null=True)
    vimeo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# events
class Event(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events/',blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)


    def __str__(self):
        return self.title

# mission
class Mission(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='mission_images/')
    quote = models.TextField()
    description1 = models.TextField(null=True)
    description2 = models.TextField(null=True)
    description3 = models.TextField(null=True)
    image2 = models.ImageField(upload_to='mission_images/', null=True)

    def __str__(self):
        return self.title

# subscriber
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

