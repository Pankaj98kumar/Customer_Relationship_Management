
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    # path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),
    path('record/<int:pk>/',views.CustomerDetails, name='record'),
    path('delete/<int:pk>/', views.DeleteRecord, name='delete'),
    path('add/', views.AddCustomer, name='add'),
    path('update/<int:pk>/', views.UpdateCustomerDetails, name='update'),
]