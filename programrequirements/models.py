from django.conf import settings
from django.db import models

# Create your models here.
class UWUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    uw_student_id = models.IntegerField()
    surname = models.CharField(max_length=32)
    given_names = models.CharField(max_length=32)
    uw_user_id = models.CharField(max_length=16)


class Course(models.Model):
    name = models.CharField(max_length=8)


class ComputerEngineering2015(models.Model):
    user = models.ForeignKey(UWUser)

    ece100a = models.BooleanField()
    che102 = models.BooleanField()
    ece105 = models.BooleanField()
    ece140 = models.BooleanField()
    ece150 = models.BooleanField()
    math117 = models.BooleanField()
    academic_standing_1a = models.CharField(max_length=16)
    extra_courses_1a = models.CharField(max_length=16)

    ece100b = models.BooleanField()
    ece103 = models.BooleanField()
    ece106 = models.BooleanField()
    ece124 = models.BooleanField()
    ece155 = models.BooleanField()
    math119 = models.BooleanField()
    academic_standing_1b = models.CharField(max_length=16)
    extra_courses_1b = models.CharField(max_length=16)

    ece200a = models.BooleanField()
    ece222 = models.BooleanField()
    ece240 = models.BooleanField()
    ece250 = models.BooleanField()
    ece290 = models.BooleanField()
    math211 = models.BooleanField()
    math215 = models.BooleanField()
    academic_standing_2a = models.CharField(max_length=16)
    extra_courses_2a = models.CharField(max_length=16)

    ece200b = models.BooleanField()
    ece207 = models.BooleanField()
    ece242 = models.BooleanField()
    ece224 = models.BooleanField()
    ece254 = models.BooleanField()
    elective_1_name = models.CharField(max_length=8)
    elective_1_value = models.BooleanField()
    academic_standing_2b = models.CharField(max_length=16)
    extra_courses_2b = models.CharField(max_length=16)

    ece300a = models.BooleanField()
    ece316 = models.BooleanField()
    ece380 = models.BooleanField()
    ece327 = models.BooleanField()
    ece351 = models.BooleanField()
    elective_2_name = models.CharField(max_length=8)
    elective_2_value = models.BooleanField()
    academic_standing_3a = models.CharField(max_length=16)
    extra_courses_3a = models.CharField(max_length=16)

    ece300b = models.BooleanField()
    ece318 = models.BooleanField()
    ece390 = models.BooleanField()
    ece356 = models.BooleanField()
    ece358 = models.BooleanField()
    elective_3_name = models.CharField(max_length=8)
    elective_3_value = models.BooleanField()
    academic_standing_3b = models.CharField(max_length=16)
    extra_courses_3b = models.CharField(max_length=16)

    ece400a = models.BooleanField()
    ece498a = models.BooleanField()
    elective_4_name = models.CharField(max_length=8)
    elective_4_value = models.BooleanField()
    elective_5_name = models.CharField(max_length=8)
    elective_5_value = models.BooleanField()
    elective_6_name = models.CharField(max_length=8)
    elective_6_value = models.BooleanField()
    elective_7_name = models.CharField(max_length=8)
    elective_7_value = models.BooleanField()
    academic_standing_4a = models.CharField(max_length=16)
    extra_courses_4a = models.CharField(max_length=16)

    ece400b = models.BooleanField()
    ece498b = models.BooleanField()
    elective_8_name = models.CharField(max_length=8)
    elective_8_value = models.BooleanField()
    elective_9_name = models.CharField(max_length=8)
    elective_9_value = models.BooleanField()
    elective_10_name = models.CharField(max_length=8)
    elective_10_value = models.BooleanField()
    elective_11_name = models.CharField(max_length=8)
    elective_11_value = models.BooleanField()
    academic_standing_4b = models.CharField(max_length=16)
    extra_courses_4b = models.CharField(max_length=16)
