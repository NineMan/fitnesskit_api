from django.db import models


class Teacher(models.Model):

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    imageUrl = models.URLField()

    def __str__(self):
        return self.short_name


class Course(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=50)
    teacher = models.CharField(max_length=255)
    startTime = models.TimeField()
    endTime = models.TimeField()
    weekDay = models.PositiveSmallIntegerField()
    appointment_id = models.CharField(max_length=50)
    service_id = models.CharField(max_length=50)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    teacher_v2 = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name='teachers_v2')
    color = models.CharField(max_length=15)
    availability = models.SmallIntegerField()

    def __str__(self):
        return self.name
