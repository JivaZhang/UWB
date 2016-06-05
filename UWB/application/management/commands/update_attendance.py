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
        cnx = mysql.connector.connect(user='sql8122262', password='l18fTReZpt', host='sql8.freemysqlhosting.net', database='sql8122262')
        query = ("SELECT * FROM attendance_data")
        cursor = cnx.cursor()
        cursor.execute(query)
        for idx, query_line in enumerate(cursor):
            print("Try to insert {} query.".format(idx))
            self._insert_row_to_database(query_line, idx)

    def _insert_row_to_database(self, line, idx):
        correction_flag = True
        try:
            lecturer = Lecturer.objects.get(first_name=line[0], last_name=line[1])
        except:
            correction_flag = False
            print("No matching lecturer with {} first name or {} last name.".format(line[0], line[1]))
        try:
            student = Student.objects.get(index_number=line[2])
        except:
            correction_flag = False
            print("No matching student with {} index number.".format(line[2]))
        if correction_flag:
            try:
                attendance = Attendance.objects.get(date=line[3], lecturer=lecturer, student=student)
                attendance.attend = line[4]
                attendance.save()
                print("Query number {} inserted correctly.".format(idx))
            except:
                print("Not found attendance with selected date.")



