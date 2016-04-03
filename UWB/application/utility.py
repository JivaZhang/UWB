from django.contrib.auth.models import User
from .models import *

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

    def _get_lecturer_data(self, lecturer):
        classes = self._get_lecturer_classes_ids(lecturer)
        attendance_by_cls = [self._get_lecturer_attendance_ids(lecturer, cls) for cls in classes]
        students_by_cls = {}
        #for attendance in attendance_by_cls:
        #student = [self._get_lecturer_students_ids(att) for att in attendance]

    def _get_lecturer_classes_ids(self, lecturer):
        return Classes.objects.filter(lecturer=lecturer)

    def _get_lecturer_attendance_ids(self, lecturer, classes):
        return Attendance.objects.filter(lecturer=lecturer, classes=classes)

    def _get_lecturer_students_ids(self, attendance):
        return attendance.student

    #@property
    #def lecturer_data(self):
    #    return self._lecturer_data
    





