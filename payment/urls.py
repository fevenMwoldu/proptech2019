from django.urls import path

from .views import ValidationView, ConfirmationView


app_name = "payment"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('c2b/validation/', ValidationView.as_view()),
    path('c2b/confirmation/', ConfirmationView.as_view()),
]