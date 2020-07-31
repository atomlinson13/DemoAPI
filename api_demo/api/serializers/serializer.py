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

def field_permission_parser(serializer_obj, table_name, *args, **kwargs):
    if 'context' in kwargs:
        if 'request' in kwargs['context']:
            request = kwargs['context']['request']

            # if request.user.is_superuser:
            #     return serializer_obj

            try:
                table = TableName.objects.get(name__iexact = table_name)
                group = request.user.groups.first()
                group_permissions = group.group_table_col_permissions.filter(table_columns__table__name = table)

                if request.method == 'GET':
                    fields = group_permissions.filter(view = False)
                elif request.method in ['PUT', 'PATCH']:
                    fields = group_permissions.filter(edit = False)
                elif request.method == 'POST':
                    fields = group_permissions.filter(create = False)
                else:
                    # delete request
                    pass

                fields = list(fields.values_list('table_columns__column__name', flat=True))

                for field in fields:
                    try:
                        serializer_obj.fields.pop(field)
                    except Exception as ex:
                        continue

            except Exception as ex:
                pass
    return serializer_obj


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
        




