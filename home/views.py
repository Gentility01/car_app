
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.core.paginator import Paginator


from .models import Product, Category
from .forms import ProductCreateForm, CategoryCreateForm

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.all()
    paginator = Paginator(product, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
        
    context = {
            'categories':categories,
            'category':category,
            # 'product':product,
            'product':page_obj
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

def category_post(request):
    c_form = CategoryCreateForm(request.POST or None)
    if c_form.is_valid():
        c_form.save()
        c_form = CategoryCreateForm()
    context = {
        'c_form':c_form
    }
    return render(request,'home/product_create.html', context)
    