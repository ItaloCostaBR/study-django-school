from django.contrib import admin

from school.models import Student, Course, Registration


# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'date_of_birth')
    list_display_links = ('id', 'name')
    search_field = 'name'
    list_per_page = 20

admin.site.register(Student, StudentsAdmin)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod_course', 'description')
    list_display_links = ('id', 'cod_course')
    search_fields = ('cod_course', 'description')
    list_per_page = 20

admin.site.register(Course, CoursesAdmin)

class RegistrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_link = 'id'
    list_per_page = 20

admin.site.register(Registration, RegistrationsAdmin)