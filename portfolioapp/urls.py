from django.urls import path
from . import views
app_name ='portfolioapp'

urlpatterns = [
    path('',views.homepage, name='homepage'),
]
