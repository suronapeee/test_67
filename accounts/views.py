#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy # new
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Create your views here.

class SignUpView(CreateView):
  #form_class = UserCreationForm
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

class ChangeView(UpdateView):
  model = CustomUser
  form_class = CustomUserChangeForm
  success_url = reverse_lazy('login')
  template_name = 'registration/change.html'
