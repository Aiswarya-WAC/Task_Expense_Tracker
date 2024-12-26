from django.urls import path
from .views import RegisterView, LoginView
from . import views
from .views import TransactionListView,TransactionCreateView



urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),  
    path('login/', views.LoginView.as_view(), name='login'),  
    path('home/', views.HomeView.as_view(), name='home'),  
    path('list/', TransactionListView.as_view(), name='transaction-list'), 
    path('add/', TransactionCreateView.as_view(), name='transaction-add'),
]

