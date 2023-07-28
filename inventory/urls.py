from django.urls import path
from . import views


app_name = "inventory"

urlpatterns = [
    path('', views.apiOverview1, name="api1-overview"),
    path('inventory-list/',views.inventoryList, name="inventory-list"),
    path('inventory-detail/<str:pk>/',views.inventoryDetail, name="inventory-detail"),
    path('inventory-update/<str:pk>/', views.inventoryUpdate, name="inventory-update"),
    path('inventory-delete/<str:pk>/', views.inventoryDelete, name="inventory-delete"),
    path("add", views.add, name="add"),
 ]