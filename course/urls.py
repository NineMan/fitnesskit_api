from django.urls import path
from .views import CourseView
from .views import SingleCourseView


app_name = 'courses'
# app  name will help us do a reverse look-up latter.

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:pk>', SingleCourseView.as_view()),
]
