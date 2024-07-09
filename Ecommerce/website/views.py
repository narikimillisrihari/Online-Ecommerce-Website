from django.shortcuts import render
from Products.models import CreateProduct

# Create your views here.
def homepage(request):
    obj=CreateProduct.objects.all()

    return render(request,'website/homepage.html',{'obj':obj})