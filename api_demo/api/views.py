from django.shortcuts import render

# Create your views here.
from api_demo.api.models import (
    Teacher, 
    Student,
    Course,
    Assignment, 
    ClassGroup,
    Grade,
    Notes,
    Attachments,
    CustomUser as User
)
from api_demo.api.serializers.serializer import (
    TeacherSerializer, 
    StudentSerializer,
    CourseSerializer,
    AssignmentSerializer,
    NotesSerializer,
    AttachmentsSerializer,
    ClassGroupSerializer,
    GradeSerializer,
    UserSerializer

)
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api_demo.api.permissions import SafeMethod, IsTeacher, IsAdmin


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)

class AssignmentList(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]
    
    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]
    
    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)

class ClassGroupList(generics.ListCreateAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ClassGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)
    
class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)


class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def get_queryset(self):
        if self.request.user.is_student:
            return self.get_queryset.filter(private = False)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def get_queryset(self):
        if self.request.user.is_student:
            return self.get_queryset.filter(private = False)

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)

class AttachmentsList(generics.ListCreateAPIView):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def get_queryset(self):
        if self.request.user.is_student:
            return self.get_queryset.filter(private = False)
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class AttachmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer
    permission_classes = [IsAuthenticated, SafeMethod | IsTeacher]

    def get_queryset(self):
        if self.request.user.is_student:
            return self.get_queryset.filter(private = False)

    def perform_update(self, serializer):
        instance = serializer.save(last_modified_by = self.request.user)
