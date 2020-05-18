from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Teacher, Course
from .serializer import CourseSerializer


class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        teacher = get_object_or_404(Teacher, name=self.request.data.get('teacher'))
        return serializer.save(teacher_v2=teacher)


class SingleCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
