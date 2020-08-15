from django.shortcuts import render, reverse
from django.views.generic import FormView

from django.contrib.auth import authenticate, login, logout

from . import forms, models, mixins

# Create your views here.


class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = ""
    form_class = None

    def form_valid(self, form):
        email = None
        password = None
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:home")
