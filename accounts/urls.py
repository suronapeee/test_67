from django.urls import path
from .views import SignUpView, ChangeView
urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
  path('change_user/<int:pk>/', ChangeView.as_view(), name='change_user'),
]
