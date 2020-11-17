from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Student(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     father_name=models.CharField(max_length=100)
#     enroll_no=models.CharField(max_length=20)
#     dob=models.DateField(null=True)

# @receiver(post_save, sender=User)
# def create_user_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_student(sender, instance, created, **kwargs):
#     instance.student.save()

# @receiver(post_save, sender=User)
# def update_user_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#     instance.student.save()
