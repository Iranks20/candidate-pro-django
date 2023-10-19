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

# features products
class Products(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_price = models.CharField(max_length=200, null=True)
    product_image = models.ImageField(upload_to='products_images/', null=True)

    def __str__(self):
        return self.product_name

# registering a user joining
class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10)
    activities = models.CharField(max_length=200, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

