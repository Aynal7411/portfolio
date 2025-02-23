from django.urls import path
from .views import consultation_form

urlpatterns = [
    path('consultation/', consultation_form, name='consultation_form'),
]
