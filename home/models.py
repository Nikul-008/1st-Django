from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply pending changes ctreated by makemigrations


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name