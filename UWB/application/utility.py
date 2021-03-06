from django.contrib.auth.models import User
from .models import *
from datetime import datetime,timedelta
from pprint import pprint

class SaveUser(object):
    def __init__(self, request):
        data = self._serialize_data(request)
        if self._is_data_valid(data):
            if self._is_index_number_in_correct_format(data['index_number']):
                self._save_user_for_login(data)
                self._save_student(data)
                self._state_of_register = True
            elif data['staff']:
                self._save_user_for_login(data)
                self._save_lecturer(data)
                self._state_of_register = True
            else:
                self._state_of_register = False
        else:
            self._state_of_register = False

    @property
    def registered(self):
        return self._state_of_register


    def _is_data_valid(self, data):
        return (data['username'] and
                data['password'] and
                data['first_name'] and
                data['last_name'])
     

    def _serialize_data(self, data):
        response = {
                'username' : data.POST['username'],
                'password' : data.POST['password'],
                'first_name' : data.POST['first_name'],
                'last_name' : data.POST['last_name'],
                'staff' : data.POST.get('staff', False),
            }
        try:
            response['index_number'] = data.POST['index_number']
        except:
            response['index_number'] = False
        return response

    def _is_index_number_in_correct_format(self, index_number):
        if index_number:
            return index_number.isdigit()
        return False

    def _save_user_for_login(self, data):
        new_user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                is_staff=data['staff']
            )
        print("Saved new user with {} name".format(data['username']))
        new_user.save()

    def _save_student(self, data):
        student = Student.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                index_number=data['index_number']
            )
        print("Saved new student with {} name".format(data['username']))
        student.save()

    def _save_lecturer(self, data):
        lecturer = Lecturer.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
            )
        print("Saved new lecturer with {} name".format(data['username']))
        lecturer.save()

class SerializeForPostSave(object):
    def __init__(self, data):
        self.POST = data

class CollectDataForLecturer(object):
    def __init__(self, lecturer):
        self._get_lecturer_data(lecturer)
        self._get_filtred_lecturer_data(lecturer)

    def _get_lecturer_data(self, lecturer):
        lecturer_name = "{} {}".format(lecturer.first_name, lecturer.last_name)
        self._lecturer_data = {'lecturer_data' : "", 'lecturer_name' : lecturer_name}
        classes = self._get_lecturer_classes_ids(lecturer)
        self._lecturer_data['lecturer_data'] = self._get_classes_name(classes)
        attendance_by_cls = [self._get_lecturer_attendance_ids(lecturer, cls) for cls in classes]
        for cls_idx, attendances in enumerate(attendance_by_cls):
            for attendance in attendances:
                student_data = self._get_lecturer_students_ids(attendance)
                self._lecturer_data['lecturer_data'][cls_idx]['classes_data'].append(
                        {
                            'first_name' : student_data.first_name,
                            'last_name' : student_data.last_name,
                            'index_number' : student_data.index_number,
                            'attendance_date' : str(attendance.date)[:-3],
                            'attendance' : attendance.attend
                        }
                    )

    def _get_filtred_lecturer_data(self, lecturer):
        actual_data = self._convert_actual_date_to_classes_begin_date()
        lecturer_name = "{} {}".format(lecturer.first_name, lecturer.last_name)
        self._lecturer_filtered_data = {'lecturer_filtred_data' : "", 'lecturer_name' : lecturer_name}
        classes = self._get_lecturer_classes_ids(lecturer)
        self._lecturer_filtered_data['lecturer_data'] = self._get_classes_name(classes)
        attendance_by_cls = [self._get_lecturer_attendance_ids_by_date(lecturer, cls, actual_data) for cls in classes]
        for cls_idx, attendances in enumerate(attendance_by_cls):
            for attendance in attendances:
                student_data = self._get_lecturer_students_ids(attendance)
                self._lecturer_filtered_data['lecturer_data'][cls_idx]['classes_data'].append(
                        {
                            'first_name' : student_data.first_name,
                            'last_name' : student_data.last_name,
                            'index_number' : student_data.index_number,
                            'attendance_date' : str(attendance.date)[:-3],
                            'attendance' : attendance.attend
                        }
                    )
        self._filter_from_empty()

    def _convert_actual_date_to_classes_begin_date(self):
        actual_data = str(datetime.now() + timedelta(hours=2))[:-16]
        classes_begin = []
        classes_begin.append(datetime.strptime(actual_data + ' 7:30', '%Y-%m-%d %H:%M'))
        classes_begin.append(datetime.strptime(actual_data + ' 9:15', '%Y-%m-%d %H:%M'))
        classes_begin.append(datetime.strptime(actual_data + ' 11:15', '%Y-%m-%d %H:%M'))
        classes_begin.append(datetime.strptime(actual_data + ' 13:15', '%Y-%m-%d %H:%M'))
        classes_begin.append(datetime.strptime(actual_data + ' 15:15', '%Y-%m-%d %H:%M'))
        classes_begin.append(datetime.strptime(actual_data + ' 17:05', '%Y-%m-%d %H:%M'))
        classes_begin.append(datetime.strptime(actual_data + ' 18:55', '%Y-%m-%d %H:%M'))
        actual_data = datetime.now() + timedelta(hours=2)
        for i in range(1,len(classes_begin)):
            if actual_data < classes_begin[i]:
                return classes_begin[i-1]
        return classes_begin[-1]

    def _filter_from_empty(self):
        filtred_classes = []
        for data in self._lecturer_filtered_data['lecturer_data']:
            if data['classes_data']:
                filtred_classes.append(data)
        self._lecturer_filtered_data['lecturer_data'] = filtred_classes


    def _get_lecturer_classes_ids(self, lecturer):
        return Classes.objects.filter(lecturer=lecturer)

    def _get_lecturer_attendance_ids_by_date(self, lecturer, classes, date):
        return Attendance.objects.filter(lecturer=lecturer, classes=classes, date=date)

    def _get_lecturer_attendance_ids(self, lecturer, classes):
        return Attendance.objects.filter(lecturer=lecturer, classes=classes)

    def _get_lecturer_students_ids(self, attendance):
        return attendance.student

    def _get_classes_name(self, classes):
        return [{'classes_data' : [], 'classes_name' : cls.name} for cls in classes] 

    @property
    def lecturer_data(self):
        return self._lecturer_data

    @property
    def lecturer_filtered_data(self):
        return self._lecturer_filtered_data

class CollectDataForStudent(object):
    def __init__(self, student):
        self._get_student_data(student)

    def _get_student_data(self, student):
        student_name = "{} {} {}".format(student.first_name, student.last_name, student.index_number)
        self._student_data = {'student_data' : [], 'student_name' : student_name}
        student_attendances = self._get_student_attendance_ids(student)
        for attendance in student_attendances:
            lecturer = self._get_lecturer_ids(attendance)
            classes = self._get_classes_ids(attendance)
            self._student_data['student_data'].append(
                    {
                        'attendance' : attendance.attend,
                        'attendance_date' : str(attendance.date)[:-3],
                        'classes_name' : classes.name,
                        'lecturer_name' : "{} {}".format(lecturer.first_name, lecturer.last_name)
                    }
                )


    def _get_student_attendance_ids(self, student):
        return Attendance.objects.filter(student=student)

    def _get_classes_ids(self, attendance):
        return attendance.classes

    def _get_lecturer_ids(self, attendance):
        return attendance.lecturer

    @property
    def student_data(self):
        return self._student_data



