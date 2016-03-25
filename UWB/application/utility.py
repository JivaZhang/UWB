from django.contrib.auth.models import User
from .models import *

class SaveUser(object):
    def __init__(self, request):
        self._state_of_register = False
        data = self._serialize_data(request)
        self._save_user_for_login(data)
        if self._is_index_number_in_correct_format(data['index_number']):
            self._save_student(data)
            self._state_of_register = True
        elif data['staff']:
            self._save_lecturer(data)
            self._state_of_register = True

    @property
    def registered(self):
        return self._state_of_register
    

    def _serialize_data(self, data):
        response = {
                'username' : data.username,
                'password' : data.password,
                'first_name' : data.first_name,
                'last_name' : data.last_name,
                'staff' : data.staff,
            }
        try:
            response['index_number'] = data.index_number
        except:
            response['index_number'] = False
        return response

    def _is_index_number_in_correct_format(index_number):
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
        new_user.save()

    def _save_student(self, data):
        student = Student.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                index_number=data['index_number']
            )
        student.save()

    def _save_lecturer(self, data):
        lecturer = Lecturer.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
            )
        lecturer.save()
