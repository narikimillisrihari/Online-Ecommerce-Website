from django.shortcuts import render,redirect
from Products.models import CreateProduct
from Products.forms import CreateProductForm
from user.models import Profile
from Products.models import CreateProduct

# Create your views here.
def create(request):
    if request.method=='POST':
        fm=CreateProductForm(request.POST, request.FILES)
        if fm.is_valid():
            product = fm.save(commit=False)
            product.posted_by = request.user.profile 
            product.save()
            return redirect('product:sellerview')
    else:
        initial_data = {
            'user': request.user,  # Example of setting a ForeignKey initial value
        }
        fm=CreateProductForm(initial=initial_data)
    return render(request,'products/create.html',{'form':fm})


def sellerview(request):
    user_id=request.user.id
    print(user_id)
    user_seller=CreateProduct.objects.filter(user_id=user_id)
    print(user_seller)
    return render(request,'products/sellerproductlist.html',{'list':user_seller})

def product_list(request):
    obj=CreateProduct.objects.all()
    return render(request,'products/productlist.html',{'obj':obj})

def product_detail(request,id):
    obj=CreateProduct.objects.get(pk=id)
    return render(request,'products/product_detail.html',{'obj':obj})


