from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=400)
    url=models.CharField(max_length=400)
    pub_date=models.DateTimeField()
    votes_total=models.IntegerField(default=1)
    images=models.ImageField(upload_to='images/')
    ico=models.ImageField(upload_to='images/')
    body=models.TextField(max_length=400)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')

    def __str__(self):
        return self.title
