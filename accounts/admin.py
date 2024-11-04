from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Specify the form to be used for adding a new user
    add_form = CustomUserCreationForm
      # Specify the form to be used for changing an existing user
    form = CustomUserChangeForm
    # Associate this admin class with the CustomUser model
    model = CustomUser


# Register the CustomUser model with the Django admin site using CustomUserAdmin
# emphasizing the use of the custom admin class.
admin.site.register(CustomUser)
