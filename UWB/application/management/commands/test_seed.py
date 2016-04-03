from django.core.management.base import BaseCommand
from datetime import datetime
from application.utility import SaveUser, SerializeForPostSave
from application.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('data_to_seed_label', nargs='*', type=int)
        parser.add_argument('-u','--user', action='store_true')

    def handle(self, *args, **options):
        if options['user']:
            self._seed_with_users()
        try:
            self._select_set(options['data_to_seed_label'][0])
        except:
            print('No set of data selected to seed')

    def _select_set(self, label):
        if label == 1:
            print('Selected first set to fill database')
            self._prepare_first_set()
        elif label == 2:
            print('Selected second set to fill database')
            self._prepare_second_set()

    def _prepare_first_set(self):
        students = Student.objects.all()
        lecturer = Lecturer.objects.all()[0]
        classes = Classes.objects.get_or_create(name='Wyklad1', lecturer=lecturer)[0]
        date = datetime(2016, 4, 26, 15, 15)
        self._set_attendance(date, students[0], lecturer, classes, True)
        self._set_attendance(date, students[1], lecturer, classes, False)
        self._set_attendance(date, students[2], lecturer, classes, False)
        self._set_attendance(date, students[3], lecturer, classes, True)


    def _prepare_second_set(self):
        students = Student.objects.all()
        lecturer = Lecturer.objects.all()[0]
        classes = Classes.objects.get_or_create(name='Wyklad1', lecturer=lecturer)[0]
        date = datetime(2016, 4, 26, 15, 15)
        self._set_attendance(date, students[0], lecturer, classes, False)
        self._set_attendance(date, students[1], lecturer, classes, True)
        self._set_attendance(date, students[2], lecturer, classes, True)
        self._set_attendance(date, students[3], lecturer, classes, False)

    def _set_attendance(self, date, student, lecturer, classes, is_attend):
        try:
            attendance = Attendance.objects.get(date=date, student=student,
                lecturer=lecturer, classes=classes)
        except:
            attendance = Attendance(date=date, attend=is_attend, student=student,
                lecturer=lecturer, classes=classes)
            attendance.save()
        else:
            attendance = Attendance.objects.filter(date=date, student=student,
                            lecturer=lecturer,
                            classes=classes).update(attend=is_attend)

    def _seed_with_users(self):
        users = []
        user = {
                'username' : 'stest1',
                'password' : 'stest1',
                'first_name' : 'stest1',
                'last_name' : 'nazwisko1',
                'staff' : False,
                'index_number' : '111111'
            }
        users.append(user)
        user = {
                'username' : 'stest2',
                'password' : 'stest2',
                'first_name' : 'stest2',
                'last_name' : 'nazwisko2',
                'staff' : False,
                'index_number' : '222222'
            }
        users.append(user)
        user = {
                'username' : 'stest3',
                'password' : 'stest3',
                'first_name' : 'stest3',
                'last_name' : 'nazwisko3',
                'staff' : False,
                'index_number' : '333333'
            }
        users.append(user)
        user = {
                'username' : 'stest4',
                'password' : 'stest4',
                'first_name' : 'stest4',
                'last_name' : 'nazwisko4',
                'staff' : False,
                'index_number' : '444444'
            }
        users.append(user)
        user = {
                'username' : 'wyk1',
                'password' : 'wyk1',
                'first_name' : 'wyk1',
                'last_name' : 'nazwiskowyk1',
                'staff' : True,
            }
        users.append(user)
        for u in users:
            SaveUser(SerializeForPostSave(u))
