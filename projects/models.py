from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=300, help_text="Comma-separated technologies used")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def tech_list(self):
        """Convert technologies into a list"""
        return self.technologies.split(',')

    def __str__(self):
        return self.title
