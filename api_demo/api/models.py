from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator
import decimal
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from django.db.models.base import ModelBase
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from api_demo.api.managers.managers import CustomUserManager
from rest_framework import serializers
from django.db.models import Q, ProtectedError
from django.db.utils import IntegrityError
# from django.contrib.auth.models import Group
import logging
import re 
logger = logging.getLogger(__name__)
from datetime import datetime, timezone as tz, date, timedelta
import math
from django.db import models
from django.contrib.auth.models import UserManager

class MyModelBase( ModelBase ):
    def __new__( cls, name, bases, attrs, **kwargs ):
        if name != "ModelName":
            if not attrs.get("Meta"):
                class MetaB:
                    db_table = name.lower()
                attrs["Meta"] = MetaB
            else:
                attrs["Meta"].db_table = name.lower()

        r = super().__new__( cls, name, bases, attrs, **kwargs )
        return r       

    class Meta:
        abstract = True

class ModelName(models.Model, metaclass = MyModelBase ):
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    name = instance.first_name.lower() + "_" + instance.last_name.lower()
    return 'profile_pictures/{0}/{1}'.format(name, filename)


class Teacher(ModelName):
    first_name = models.CharField('First Name', max_length=256, null=False, blank=True)
    last_name = models.CharField('Last Name', max_length=256, null=False, blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True, default = '/default_images/profile_picture.png')
    email = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=False, blank=True)
    creator = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, related_name="teaher_creator", null=True, blank=True)
    last_modified_by = models.ForeignKey('CustomUser', null=True, blank=True, on_delete=models.SET_NULL, related_name="teaher_last_modified_by")
 
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(ModelName):
    name = models.CharField(max_length=256, null=False, blank=True)
    teacher = models.ForeignKey(Teacher, null=False, blank=True, on_delete=models.CASCADE)
    creator = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, related_name="class_creator", null=True, blank=True)
    last_modified_by = models.ForeignKey('CustomUser', null=True, blank=True, on_delete=models.SET_NULL, related_name="class_last_modified_by")
    students = models.ManyToManyField('Student')

class Student(ModelName):
    first_name = models.CharField('First Name', max_length=256, null=False, blank=True)
    last_name = models.CharField('Last Name', max_length=256, null=False, blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True, default = '/default_images/profile_picture.png')
    student_id = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=False, blank=True)
    creator = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, related_name="student_creator", null=True, blank=True)
    last_modified_by = models.ForeignKey('CustomUser', null=True, blank=True, on_delete=models.SET_NULL, related_name="student_last_modified_by")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ClassGroup(ModelName):
    name = models.CharField('Name', max_length=256, null=False, blank=True)
    def __str__(self):
        return f'{self.name}'


class Grade(ModelName):
    name = models.CharField('Name', max_length=256, null=False, blank=True)
    grade_recieved = models.IntegerField(default=0)
    assignment = models.ForeignKey('Assignment', null=True, blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey(ClassGroup, null=True, blank=True, on_delete=models.CASCADE)
    creator = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, related_name="grade_creator", null=True, blank=True)
    last_modified_by = models.ForeignKey('CustomUser', null=True, blank=True, on_delete=models.SET_NULL, related_name="grade_last_modified_by")

    def __str__(self):
        return f'{self.name}'

def attachment_directory_path(instance, filename):
    return 'class/{cid}/assignment/{aid}/{doc}'.format(cid=instance.school_class.id, aid =instance.id,  doc=filename)

class Assignment(ModelName): 
    name = models.CharField('Name', blank=True, null=True, max_length=250)
    description = models.CharField('Name', blank=True, null=True, max_length=250)
    doc = models.FileField(upload_to=attachment_directory_path, null=True)
    assignment_type = "individual" "group"
    weight = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)


class AccountType(ModelName): 
    name = models.CharField('Name', blank=True, null=True, max_length=50)

    def __str__(self):
        return f"{self.name}"



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    last_modified_by = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, related_name="last_modified_by_user")
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.PROTECT, related_name="user_contact")
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    account_type = models.ForeignKey(AccountType, null=True, blank=True, on_delete=models.PROTECT)    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "user"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    @property
    def is_student(self): 
        return self.account_type.name == 'student'

    @property
    def is_teacher(self): 
        return self.account_type.name == 'teacher'

class Notes(ModelName):
    creator = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="note_creator")
    last_modified_by = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="notes_last_modified_by")
    note = models.CharField(blank=True, null=False, max_length=4096) 
    assignment = models.ForeignKey(Assignment, null=True, blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey(ClassGroup, null=True, blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, null=True, blank=True, on_delete=models.CASCADE)
    private = models.BooleanField(null=False, blank=True, default=False)

    def __str__(self):
        return self.note

    class Meta:
        verbose_name_plural = "Notes"


class Attachments(ModelName):
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="attachment_creator", null=True, blank=True)
    last_modified_by = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="attachments_last_modified_by")
    name = models.CharField('Name', blank=True, null=False, max_length=500)
    description = models.CharField('Description', blank=True, null=True, max_length=1024)
    assignment = models.ForeignKey(Assignment, null=True, blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey(ClassGroup, null=True, blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, null=True, blank=True, on_delete=models.CASCADE)
    private = models.BooleanField(null=False, blank=True, default=False)
    link = models.FileField(upload_to=attachment_directory_path, null=True)
    private = models.BooleanField(null=False, blank=True, default=False)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Attachments"
