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
