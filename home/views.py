
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView


from .models import Product, Category
from .forms import ProductCreateForm

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
        
    context = {
            'categories':categories,
            'category':category,
            'product':product
        }
    return render(request, 'home/article_list.html', context)
    
    
def product_detail(request, id):
    product  = get_object_or_404(Product, id=id)
    context = {
        'product':product
    }
    return render(request, 'home/productdetail.html', context)


def  create_post(request):
    form = ProductCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = {
        'form':form
    }
    return render(request,'home/product_create.html', context)
    