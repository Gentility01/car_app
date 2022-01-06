from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    # home_view,
  
    product_list,
    product_detail,
    create_post
    # ProductCreateView
   
    
)

app_name = 'product'

urlpatterns = [
    # path('', home_view, name='homeview'),
    # path('product_create', ProductCreateView.as_view(), name='product_create'),
    path('', product_list, name='product_list'),
    path('create_post/', create_post, name='create_post'),
    path('product_list/<slug:category_slug>/', product_list, name='product_list_category'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    
