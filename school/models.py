from django.db import models

# Create your models here.


class School(models.Model):

    school_name = models.CharField(max_length=100)
    school_motto = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name


class Classroom(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classroom_title = models.CharField(max_length=100)
    classroom_grade = models.IntegerField()

    def __str__(self):
        return "%s in %s" % (self.classroom_title, self.school)


class Student(models.Model):

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date_of_birth = models.DateField('student date of birth')

    def __str__(self):
        return "%s %s in %s" % (
            self.first_name, self.last_name, self.classroom
        )
