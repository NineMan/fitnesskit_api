from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView

from .models import Teacher, Course
from .serializer import CourseSerializer


class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        teacher_v2 = get_object_or_404(Teacher, id=self.request.data.get('teacher_id'))
        return serializer.save(teacher_v2=teacher_v2)
