from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
    products=Product.objects
    return render(request, 'product/home.html',{'products':products})

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['images'] and request.FILES['ico'] :
            product= Product()
            product.title= request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http//:') or request.POST['url'].startswith('https//:'):
                product.url=request.POST['url']
            else:
                product.url="http//:" + request.POST['url']

            product.images= request.FILES['images']
            product.ico=request.FILES['ico']

            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            return render(request, 'product/create.html',{'error':'All fields are not field'})


    else:
        return render(request, 'product/create.html')


def detail(request, product_id):
    product=get_object_or_404(Product, pk=product_id)
    return render(request ,'product/detail.html',{'product':product})


@login_required
def upvote(request, product_id):
    if request.method=='POST':

        product=get_object_or_404(Product, pk=product_id)
        product.votes_total+=1
        product.save()

        return redirect('/products/'+str(product.id))
