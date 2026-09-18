from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    modules_count = models.PositiveIntegerField(default=0)
    students_count = models.PositiveIntegerField(default=0)
    progress = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title