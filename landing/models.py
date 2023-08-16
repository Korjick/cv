import os.path
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


class Course(models.Model):
    title = models.TextField()
    institution = models.TextField()
    institution_url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=PathAndRename('course/'), null=True)
    started = models.DateField()
    ended = models.DateField(blank=True, null=True)


class Proud(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to=PathAndRename('course/'), null=True)


class Education(models.Model):
    title = models.TextField()
    grade = models.IntegerField()
    institution = models.TextField()
    institution_url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=PathAndRename('education/'), null=True)
    started = models.DateField()
    ended = models.DateField(blank=True, null=True)


class Experience(models.Model):
    title = models.TextField()
    company = models.TextField()
    company_url = models.URLField(blank=True, null=True)
    started = models.DateField()
    ended = models.DateField(blank=True, null=True)
    location = models.TextField()

    def __str__(self):
        return str(self.title)


class Duty(models.Model):
    title = models.TextField()
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='duties')


class HardSkill(models.Model):
    title = models.TextField()


class SoftSkill(models.Model):
    title = models.TextField()


class Language(models.Model):
    title = models.TextField()
    level = models.TextField()


class Referee(models.Model):
    title = models.TextField()
    job_title = models.TextField()
    email = models.EmailField()
    address = models.TextField()