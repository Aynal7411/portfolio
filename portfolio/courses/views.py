from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment
# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# View for course details
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

from .forms import EnrollmentForm
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()
            return redirect('course_list')  # Redirect to course list after enrollment
    else:
        form = EnrollmentForm()

    return render(request, 'enroll_in_course.html', {'form': form, 'course': course})