from django.db import models

class Consultation(models.Model):
    SERVICE_CHOICES = [
        ('web_dev', 'Web Development'),
        ('app_dev', 'App Development'),
        ('ai', 'AI Services'),
        ('machine learning', 'Machine Learning'),
        ('data_science', 'Data Science'),
        ('other','Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    business_name = models.CharField(max_length=150, blank=True, null=True)  # Business name
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='other')  # Type of service
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Estimated budget
    preferred_date = models.DateField(blank=True, null=True)  # Preferred consultation date
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
