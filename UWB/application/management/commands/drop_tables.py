from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from application.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u','--user', action='store_true')
        parser.add_argument('-s','--student', action='store_true')
        parser.add_argument('-l','--lecturer', action='store_true')
        parser.add_argument('-c','--classes', action='store_true')
        parser.add_argument('-a','--attendance', action='store_true')
        parser.add_argument('--all', action='store_true')

    def handle(self, *args, **options):
        self._select_tables_to_drop(options)

    def _select_tables_to_drop(self, label):
        if label['all']:
            self._drop_attendance('attendance')
            self._drop_classes('classes')
            self._drop_authorization_user('authorization')
            self._drop_student_user('student')
            self._drop_lecturer_user('lecturer')
        else:
            if label['attendance']:
                self._drop_attendance('attendance')
            if label['classes']:
                self._drop_classes('classes')
            if label['user']:
                self._drop_authorization_user('authorization')
            if label['student']:
                self._drop_student_user('student')
            if label['lecturer']:
                self._drop_lecturer_user('lecturer')

    def _drop_authorization_user(self, kind_of_user):
        for i in User.objects.all():
            print(i.delete())
        print("{} users table is empty now".format(kind_of_user.title()))

    def _drop_student_user(self, kind_of_user):
        for i in Student.objects.all():
            print(i.delete())
        print("{} users table is empty now".format(kind_of_user.title()))

    def _drop_lecturer_user(self, kind_of_user):
        for i in Lecturer.objects.all():
            print(i.delete())
        print("{} users table is empty now".format(kind_of_user.title()))

    def _drop_attendance(self, label_name):
        for i in Attendance.objects.all():
            print(i.delete())
        print("{} table is empty now".format(label_name.title()))

    def _drop_classes(self, label_name):
        for i in Classes.objects.all():
            print(i.delete())
        print("{} table is empty now".format(label_name.title()))