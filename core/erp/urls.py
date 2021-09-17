from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.contact.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.product.views import *

app_mame = 'erp'

urlpatterns = [
    #Contacts(borrar)
    path('contact/view/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    #Contact
    path('contact/list/', ContactListView.as_view(), name='contact_list'),
    path('contact/add/', ContactCreateView.as_view(), name='contact_create'),
    path('contact/edit/<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('contact/delete/<int:pk>/', ContactDeleteView.as_view(), name='contact_delete'),
    path('contact/form/', ContactFormView.as_view(), name='contact_form'),
    #Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #Category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    #Product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]