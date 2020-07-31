from rest_framework import serializers
from api_demo.api.models import (
    Teacher,
    Course,
    Student,
    ClassGroup,
    Grade,
    Assignment,
    CustomUser as User,
    AccountType,
    Notes,
    Attachments,
)
from django.db.models import Q
from django.db.utils import IntegrityError


import logging
logger = logging.getLogger(__name__)
from django.db.models.query import QuerySet
from django.utils import timezone


class ClassGroupSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = ClassGroup
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']


class GradeSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Grade
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']

class AccountTypeSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = AccountType
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']

class TeacherSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']

class StudentSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']


class CourseSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']


class AssignmentSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Assignment
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']

class NotesSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Notes
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']

class AttachmentsSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 

    class Meta:
        model = Attachments
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']


class UserSerializer(serializers.ModelSerializer): 
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    modified_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M UTC", required=False, read_only=True) 
    account_type = AccountTypeSerializer()
    
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['creator', 'last_modified_by', 'created_date', 'last_modified_by']
        




