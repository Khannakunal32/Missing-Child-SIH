from src.models.citizen_database import CitizenLogin
from src.models.citizen_database import CitizenDetails
from src.models.citizen_database import CitizenAddress
from time import sleep

def create_account(registration_info):
    emailId = registration_info.get('emailId', None)
    password = registration_info.get('password', None)
    firstName = registration_info.get('firstName', None)
    middleName = registration_info.get('middleName', None)
    lastName = registration_info.get('lastName', None)
    phoneNumber = registration_info.get('phoneNumber', None)
    governmentId = registration_info.get('governmentId', None)
    street = registration_info.get('street', None)
    city = registration_info.get('city', None)
    state = registration_info.get('state', None)
    country = registration_info.get('country', None)
    zip_code = registration_info.get('zip_code', None)

    registrationStatus = True
    message = 'Registered Successfully'

    login = False
    details = False
    address = False

    try:
        citizen_login = CitizenLogin()
        citizen_login.emailId = emailId
        citizen_login.password = password
        citizen_login.save()
        login = True

        citizen_details = CitizenDetails()
        citizen_details.emailId = emailId
        citizen_details.firstName = firstName
        if middleName: citizen_details.middleName = middleName
        if lastName: citizen_details.lastName = lastName
        citizen_details.phoneNumber = phoneNumber
        if governmentId: citizen_details.governmentId = governmentId
        citizen_details.save()
        details = True

        citizen_address = CitizenAddress()
        citizen_address.emailId = emailId
        citizen_address.street = street
        citizen_address.city = city
        citizen_address.state = state
        if country: citizen_address.country = country
        citizen_address.zip_code = zip_code
        citizen_address.save()
        address = True
    
    except:
        if login:
            citizen_login = CitizenLogin.objects(emailId=emailId).first().delete()
        
        if details:
            citizen_details = CitizenDetails.objects(emailId=emailId).frst().delete()
        
        if address:
            citizen_address = CitizenAddress.objects(emailId=emailId).frst().delete()

        registrationStatus = False
        message = 'Error'
    
    registration_info['registrationStatus'] = registrationStatus
    registration_info['message'] = message

def registration(registration_info):
    emailId = registration_info['emailId']
    citizen = CitizenLogin.objects(emailId=emailId)
    # citizen = []
    # sleep(3)
    registration_info['registrationStatus'] = None
    registration_info['message'] = None

    if len(citizen):
        registration_info['registrationStatus'] = False
        registration_info['message'] = 'User Exist'

    else:
        create_account(registration_info=registration_info)
    
    return registration_info


