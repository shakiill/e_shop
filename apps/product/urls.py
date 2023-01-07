from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('add/', views.ProductAddView.as_view(), name='product_add'),
]
