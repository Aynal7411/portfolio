from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Consultation
from .forms import ConsultationForm

def consultation_form(request):
    
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your  consultation request has been submitted successfully!")
            return redirect('consultation_form')  # Redirect to the same page after submission
    else:
        form = ConsultationForm()
    
    return render(request, 'consultation_form.html', {'form': form})

