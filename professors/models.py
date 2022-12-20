from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True, null=True)

    def getAverageRate(self):
        sum = 0.0
        count = self.course_set.count()
        if count <= 0:
            return 0
        for course in self.course_set.all():
            sum += course.getAverageRate()
        return sum / count
    
    def getNumOfRatings(self):
        sum = 0
        count = self.course_set.count()
        if count <= 0:
            return 0
        for course in self.course_set.all():
            sum += course.rating_set.count()
        return sum

    def __str__(self):
        return self.name

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    course_number = models.CharField(max_length=20, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def getAverageRate(self):
        if self.rating_set.count() <= 0:
            return 0
        return self.rating_set.aggregate(Avg('rate'))['rate__avg']

    def __str__(self):
        return self.subject + self.course_number


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    major = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=30)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rate = models.IntegerField()
    attendance = models.BooleanField(null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(default='')