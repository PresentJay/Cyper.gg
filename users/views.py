from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from django.contrib.auth import authenticate, login, logout

from . import forms, models, mixins

# Create your views here.


class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = ""
    form_class = None
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = None
        password = None
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:home")


class SignUpView(mixins.LoggedOutOnlyView, FormView):
    template_name = ""
    form_class = None
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        # need form save
        email = None
        password = None
        user = authenticate(self.request, username=email, password=password)
        
        if user is not None:
            login(self.request, user)
            
        # need verify email
        
        return super().form_valid(form)
    
    
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))