
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Transaction
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if not username or not password or not confirmpassword or not email:
            return HttpResponse("<script>alert('All fields are required'); window.location='/register'</script>")

        if password != confirmpassword:
            return HttpResponse("<script>alert('Passwords do not match'); window.location='/register'</script>")

        if User.objects.filter(username=username).exists():
            return HttpResponse("<script>alert('Username already exists'); window.location='register'</script>")

        if User.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('Email already exists'); window.location='/register'</script>")

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse("<script>alert('Registration Successful! Please login.'); window.location='/login#m'</script>")


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # next_page = request.GET.get('next')  # Check if there's a 'next' parameter
            # if next_page:
            #     return redirect(next_page)  # Redirect to the next page if available
            return HttpResponse("<script>alert('Login Successful!'); window.location='/home'</script>")  # Redirect to home page
        else:
            return HttpResponse("<script>alert('Invalid username or password'); window.location='/login#m'</script>")


class HomeView(LoginRequiredMixin, View):  # Restrict access to authenticated users
    def get(self, request):
        return render(request, 'home.html')
    
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'

class TransactionCreateView(View):
    def get(self, request):
        return render(request, 'transaction_form.html')

    def post(self, request):
        transaction_type = request.POST.get('transaction_type')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')

      
        transaction = Transaction.objects.create(
            transaction_type=transaction_type,
            amount=amount,
            category=category,
            date=date
        )
        transaction.save()
        return HttpResponse("<script>alert('Transaction added successfully!'); window.location='/add'</script>")