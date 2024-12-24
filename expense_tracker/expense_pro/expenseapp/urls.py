from django.urls import path
from .views import RegisterView, LoginView
from . import views
from .views import TransactionListView,TransactionCreateView



urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),  # Register page
    path('login/', views.LoginView.as_view(), name='login'),  # Login page
    path('home/', views.HomeView.as_view(), name='home'),  # Home page
    path('list/', TransactionListView.as_view(), name='transaction-list'),  # View all transactions
    path('add/', TransactionCreateView.as_view(), name='transaction-add'),
]

