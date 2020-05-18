from rest_framework import serializers
from .models import Teacher, Course


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name',
                  'short_name',
                  'position',
                  'imageUrl']


class CourseSerializer(serializers.ModelSerializer):

    teacher_v2 = TeacherSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['name',
                  'description',
                  'place',
                  'teacher',
                  'startTime',
                  'endTime',
                  'weekDay',
                  'appointment_id',
                  'service_id',
                  'pay',
                  'appointment',
                  'teacher_v2',
                  'color',
                  'availability']
