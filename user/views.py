from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login

from settings.models import *
from dishes.models import *
from user.forms import *

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration-page.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')