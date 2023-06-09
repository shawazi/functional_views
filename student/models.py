from django.db import models

# Create your models here.
class Path(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

