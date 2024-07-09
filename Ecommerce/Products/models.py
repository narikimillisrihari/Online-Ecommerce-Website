from django.db import models
from user.models import Profile

# Create your models here.
class CreateProduct(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='product_images/')
    posted_date=models.DateTimeField(auto_now_add=True)