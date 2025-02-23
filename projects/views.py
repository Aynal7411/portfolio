from django.shortcuts import render,get_object_or_404
from .models import Project
# Create your views here.
def my_projects(request):
    projects = Project.objects.all().order_by('-created_at')

    return render(request,'project.html', {'projects': projects})

def project_detail_page(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'project': project})