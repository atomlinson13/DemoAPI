from django.contrib import admin, auth
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
    Attachments
)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'note', 'creator', 'created_date', 'private']
    ordering = ['id']

@admin.register(Attachments)
class AttachmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'creator', 'created_date', 'private']
    ordering = ['id']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    ordering = ['id']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'first_name', 'last_name', 'email']
    ordering = ['id']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'teacher']
    ordering = ['id']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'grade_recieved', 'assignment', 'student', 'group']
    ordering = ['id']
    
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'assignment_type', 'weight', 'course']
    ordering = ['id']


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def full_name(self, obj):
        print(obj.__dict__)
        return "Hello"
        # if obj.account_type.name.lower() == 'teacher':  
        #     return f"{obj.teacher.first_name} {obj.teacher.last_name}" 
        # else:
        #     return f"{obj.student.first_name} {obj.student.last_name}" 

    list_display = ['id', 'full_name', 'email', 'account_type']
