Wersja pythona - python3
Wersja django - 1.9.x
Instalacja
sudo apt-get install pip3
pip3 install django mysqlclient
mysql -u root
create database uwb;
python3 manage.py makemigrations
python3 manage.py migrate
Jak nie macie mysql:
sudo apt-get install mysql-server
Nazwy tabel to: application_xxx

