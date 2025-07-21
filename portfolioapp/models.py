from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    live_url = models.URLField(null=True, blank=True)
    code_url = models.URLField(null=True, blank=True)
    tech_stack = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
