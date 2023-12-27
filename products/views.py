from django.shortcuts import render
from .models import Products,Feedback
from .forms import FeedbackForm
from django.contrib import messages

# Create your views here.

def index(request):
    products = Products.objects.all().order_by("id")[:4]
    return render(request, "products/home.html",{
        "products": products,
    })
 
def signup(request):
    return render (request,"products/signup.html")


def product_page(request,product_brand,product_slug):
    product = Products.objects.get(slug = product_slug)
    form = FeedbackForm()
    reviews = Feedback.objects.filter(products = product)
    if request.method  == "GET":
        return render(request, "products/product.html",{
        'product':product,
        'form':form,
        'reviews':reviews,   
    })
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                name =  form.cleaned_data["name"],
                rating =  form.cleaned_data["rating"],
                products =  product,
                text =  form.cleaned_data["text"]
            ) 
            feedback.save()
            messages.success(request,"Your Feedback has Reached Us")
            print(form.cleaned_data)
        return render(request, "products/product.html",{
        'product': product,
        'form': form,
        'reviews': reviews,
    })

def catlog(request):
    product = Products.objects.all()
    return render (request, "products/allProduct.html",{
        "product":product,
    })