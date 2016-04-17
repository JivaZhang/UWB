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
        classes1 = Classes.objects.get_or_create(name='Wyklad1', lecturer=lecturer)[0]
        classes2 = Classes.objects.get_or_create(name='Wyklad2', lecturer=lecturer)[0]
        classes3 = Classes.objects.get_or_create(name='Wyklad3', lecturer=lecturer)[0]
        date1 = datetime(2016, 4, 17, 7, 30)
        date2 = datetime(2016, 4, 17, 9, 15)
        date3 = datetime(2016, 4, 17, 11, 15)
        #
        self._set_attendance(date1, students[0], lecturer, classes1, True)
        self._set_attendance(date1, students[1], lecturer, classes1, False)
        self._set_attendance(date1, students[2], lecturer, classes1, False)
        self._set_attendance(date1, students[3], lecturer, classes1, True)
        #
        self._set_attendance(date2, students[0], lecturer, classes2, True)
        self._set_attendance(date2, students[1], lecturer, classes2, True)
        self._set_attendance(date2, students[2], lecturer, classes2, True)
        self._set_attendance(date2, students[3], lecturer, classes2, False)
        #
        self._set_attendance(date3, students[0], lecturer, classes3, False)
        self._set_attendance(date3, students[1], lecturer, classes3, False)
        self._set_attendance(date3, students[2], lecturer, classes3, False)
        self._set_attendance(date3, students[3], lecturer, classes3, False)


    def _prepare_second_set(self):
        students = Student.objects.all()
        lecturer = Lecturer.objects.all()[0]
        classes1 = Classes.objects.get_or_create(name='Wyklad1', lecturer=lecturer)[0]
        classes2 = Classes.objects.get_or_create(name='Wyklad2', lecturer=lecturer)[0]
        classes3 = Classes.objects.get_or_create(name='Wyklad3', lecturer=lecturer)[0]
        date1 = datetime(2016, 4, 17, 7, 30)
        date2 = datetime(2016, 4, 17, 9, 15)
        date3 = datetime(2016, 4, 17, 11, 15)
        #
        self._set_attendance(date1, students[0], lecturer, classes1, False)
        self._set_attendance(date1, students[1], lecturer, classes1, True)
        self._set_attendance(date1, students[2], lecturer, classes1, True)
        self._set_attendance(date1, students[3], lecturer, classes1, False)
        #
        self._set_attendance(date2, students[0], lecturer, classes2, False)
        self._set_attendance(date2, students[1], lecturer, classes2, False)
        self._set_attendance(date2, students[2], lecturer, classes2, False)
        self._set_attendance(date2, students[3], lecturer, classes2, True)
        #
        self._set_attendance(date3, students[0], lecturer, classes3, True)
        self._set_attendance(date3, students[1], lecturer, classes3, True)
        self._set_attendance(date3, students[2], lecturer, classes3, False)
        self._set_attendance(date3, students[3], lecturer, classes3, True)


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
