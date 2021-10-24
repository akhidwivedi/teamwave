from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('questions/', views.ItemsList.as_view()),

]
    

urlpatterns = format_suffix_patterns(urlpatterns)