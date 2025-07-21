from django.urls import path
from .views import contact_view

urlpatterns = [
    path('submit-contact/', contact_view, name='contact'),  # handles POST from form
]
