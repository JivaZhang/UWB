from django.core.management.base import BaseCommand
from datetime import datetime
from application.models import *
import mysql.connector

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f','--force', action='store_true')

    def handle(self, *args, **options):
        self._read_and_parse_data()

    def _read_and_parse_data(self):
        cnx = mysql.connector.connect(user='sql7116257', password='jsQjPHmC25', host='sql7.freemysqlhosting.net', database='sql7116257')
        query = ("SELECT * FROM attendance_data")
        cursor = cnx.cursor()
        cursor.execute(query)
        for idx, query_line in enumerate(cursor):
            print("Try to insert {} query.".format(idx))
            self._insert_row_to_database(query_line, idx)

    def _insert_row_to_database(self, line, idx):
        correction_flag = True
        try:
            classes = Classes.objects.get(name=line[0])
        except:
            correction_flag = False
            print("No matching classes with {} name.".format(line[0]))
        try:
            lecturer = Lecturer.objects.get(first_name=line[1], last_name=line[2])
        except:
            correction_flag = False
            print("No matching lecturer with {} first name or {} last name.".format(line[1], line[2]))
        try:
            student = Student.objects.get(index_number=line[3])
        except:
            correction_flag = False
            print("No matching student with {} index number.".format(line[3]))
        if correction_flag:
            try:
                attendance = Attendance.objects.get(date=line[4], classes=classes, lecturer=lecturer, student=student)
                attendance.attend = line[5]
                attendance.save()
                print("Query number {} inserted correctly.".format(idx))
            except:
                print("Not found attendance with selected date.")



