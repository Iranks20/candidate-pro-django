from django.db import models

class Campaign(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.TextField()
    background_image = models.ImageField(upload_to='campaign_backgrounds/', null=True)

    def __str__(self):
        return self.title
