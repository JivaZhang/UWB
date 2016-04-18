from django.core.management.base import BaseCommand
from datetime import datetime
from application.models import *
import csv
import os

FILENAME = "/home/pawel/Workshop/gosp/UWB/attendance_data/DATA.csv"
LOCK = "/home/pawel/Workshop/gosp/UWB/attendance_data/LOCK"

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f','--force', action='store_true')

    def handle(self, *args, **options):
        if self._is_lock_exist():
            print("LOCK file exist")
        else: 
            self._put_lock()
            try:
                self._read_and_parse_data()
                self._remove_file_data()
            except:
                pass
            finally:
                self._remove_lock()

    def _read_and_parse_data(self):
        with open(FILENAME, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if len(row) == 6:
                    self._insert_row_to_database(row)

    def _is_lock_exist(self):
        try:
            with open(LOCK, 'r') as lock:
                pass
            return True
        except:
            return False

    def _put_lock(self):
        with open(LOCK, 'w') as lock:
            pass

    def _remove_lock(self):
        os.remove(LOCK)

    def _remove_file_data(self):
        os.remove(FILENAME)

    def _convert_attendance(self, field):
        if field.lower() == "true":
            return True
        elif field.lower() == "false":
            return False

    def _convert_date(self, date):
        return datetime.strptime(date, '%d-%m-%Y %H:%M')

    def _insert_row_to_database(self, line):
        line[4] = self._convert_date(line[4][:])
        line[5] = self._convert_attendance(line[5][:])
        classes = Classes.objects.get(name=line[0])
        lecturer = Lecturer.objects.get(first_name=line[1], last_name=line[2])
        student = Student.objects.get(index_number=line[3])
        attendance = Attendance.objects.get(date=line[4], classes=classes, lecturer=lecturer, student=student)
        attendance.attend = line[5]
        attendance.save()



