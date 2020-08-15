from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyView(UserPassesTestMixin):
    def PermitionException(self):
        return redirect("core:home")


class LoggedOutOnlyView(UserPassesTestMixin):
    def PermitionException(self):
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")
