from src.services import citizen_services
from src.services import police_services
from src.services import common_services

def citizen_registration():
    regis = [['rajivk@gmail.com', 'rajiv@123', 'Rajiv', None, 'Kumar', 9999999999, 'Kamal Street', 'Kathgodam', 'Uttrakhand', 263126],
    ['sheetalg@gmail.com', 'sheetal@123', 'Sheetal', None, 'Gupta', 8888888888, 'Surya Nagar', 'Ghaziabad', 'Uttar Pradesh', 201010],
    ['anna@gmail.com', 'anna@123', 'Anna', None, None, 7777777777, 'Chander Nagar', 'Ghaziabad', 'Uttar Pradesh', 201011]]
    for r in regis:
        regis_info = dict()
        regis_info['emailId'] = r[0]
        regis_info['password'] = r[1]
        regis_info['firstName'] = r[2]
        regis_info['middleName'] = r[3]
        regis_info['lastName'] = r[4]
        regis_info['phoneNumber'] = r[5]
        regis_info['street'] = r[6]
        regis_info['city'] = r[7]
        regis_info['state'] = r[8]
        regis_info['zip_code'] = r[9]
        print(citizen_services.registration(regis_info))

def police_registration():
    regis = [['P01', 'p01@123', 'Bahadur Singh', 9988888889, 'Kamal Street', 'Kathgodam', 'Uttrakhand', 263126, 'Kathgodam'],
    ['P02', 'p02@123', 'Shivaji', 8888999999, 'Surya Nagar', 'Ghaziabad', 'Uttar Pradesh', 201010, 'Ghaziabad'],
    ['P03', 'p03@123', 'Raunaq', 7777766666, 'Chander Nagar', 'Noida', 'Uttar Pradesh', 201011, 'Noida']]
    for r in regis:
        regis_info = dict()
        regis_info['pId'] = r[0]
        regis_info['password'] = r[1]
        regis_info['shoName'] = r[2]
        regis_info['shoNumber'] = r[3]
        regis_info['street'] = r[4]
        regis_info['city'] = r[5]
        regis_info['state'] = r[6]
        regis_info['zip_code'] = r[7]
        regis_info['zone'] = r[8]
        print(police_services.registration(regis_info))

def child_registration():
    pass

if __name__ == '__main__':
    citizen_registration()
    police_registration()
    child_registration()
