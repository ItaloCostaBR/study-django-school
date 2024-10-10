from rest_framework import serializers

from school.models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['cod_course', 'description', 'level']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        # exclude = [] or fields = '__all__'
        exclude = []

class StudentRegistrationsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()

class RegistrationStudentsSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student_name']