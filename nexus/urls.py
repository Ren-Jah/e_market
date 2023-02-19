from django.urls import path
from nexus import views

urlpatterns = [
    path("element/create", views.ElementCreateView.as_view()),
    path("element/list", views.ElementListView.as_view()),
    path("element/<pk>", views.ElementView.as_view()),
    path("product/create", views.ProductInfoCreateView.as_view()),
    path("product/list", views.ProductInfoListView.as_view()),
    path("product/<pk>", views.ProductInfoView.as_view()),
]
