from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, \
    StudentRegistrationsSerializer, RegistrationStudentsSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ Show all students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    """ Show all courses """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentRegistrations(generics.ListAPIView):
    """ List of student registrations """
    def get_queryset(self):
        queryset = Registration.objects.filter(student__id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentRegistrationsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationStudentsInCourse(generics.ListAPIView):
    """ List of registration students """
    def get_queryset(self):
        queryset = Registration.objects.filter(course__id=self.kwargs['pk'])
        return queryset
    serializer_class = RegistrationStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]