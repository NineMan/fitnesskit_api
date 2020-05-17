from django.db import models


class Teacher(models.Model):

    POSITION = [
        ('Master-trainer of GP', 'Master-trainer of GP'),
        ('Any other position', 'Any other position'),
    ]

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100, choices=POSITION)
    imageUrl = models.URLField()

    def __str__(self):
        return self.short_name


class Course(models.Model):

    STUDIOS = [
        ('Студия 1', 'Студия 1'),
        ('Студия 7', 'Студия 7'),
    ]
    TEACHERS = [
        ('Smith Helen', 'Smith Helen'),
        ('another teacher', 'another teacher'),
    ]
    WEEKDAY = [
        (1, 'ПН'),
        (2, 'ВТ'),
        (3, 'СР'),
        (4, 'ЧТ'),
        (5, 'ПТ'),
        (6, 'СБ'),
        (7, 'ВС'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=50, choices=STUDIOS)
    teacher = models.CharField(max_length=255, choices=TEACHERS)
    startTime = models.TimeField()
    endTime = models.TimeField()
    weekDay = models.PositiveSmallIntegerField(choices=WEEKDAY)
    appointment_id = models.CharField(max_length=50)
    service_id = models.CharField(max_length=50)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    teacher_v2 = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name='teachers_v2')
    color = models.CharField(max_length=15)
    availability = models.SmallIntegerField()

    def __str__(self):
        return self.name
