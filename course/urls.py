from django.urls import path
from .views import CourseView


app_name = 'courses'
# app  name will help us do a reverse look-up latter.

urlpatterns = [
    path('courses/', CourseView.as_view()),
]
