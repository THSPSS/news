from django.db import models
from datetime import datetime

# Create your models here.
# representation or database schema
# converting table to python object
# delete , updating or fetching ect

# set as database table
#after change in this file in migrations folder there is another initial file


class Listing(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=300)
    # picture is quiet complicate to decide now so i leave it as comment
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    



