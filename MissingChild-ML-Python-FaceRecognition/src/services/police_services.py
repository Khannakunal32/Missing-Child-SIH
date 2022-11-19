from src.models.police_database import PoliceLogin
from src.models.police_database import PoliceStationDetails
from src.models.police_database import PoliceStationAddress

def create_account(registration_info):
    pId = registration_info.get('pId', None)
    password = registration_info.get('password', None)
    shoName = registration_info.get('shoName', None)
    shoNumber = registration_info.get('shoNumber', None)
    street = registration_info.get('street', None)
    city = registration_info.get('city', None)
    state = registration_info.get('state', None)
    country = registration_info.get('country', 'INDIA')
    zip_code = registration_info.get('zip_code', None)
    zone = registration_info.get('zone', None)

    registrationStatus = True
    message = 'Registered Successfully'

    login = False
    details = False
    address = False

    try:
        police_login = PoliceLogin()
        police_login.pId = pId
        police_login.password = password
        police_login.save()
        login = True

        police_station_details = PoliceStationDetails()
        police_station_details.pId = pId
        police_station_details.shoName = shoName
        police_station_details.shoNumber = shoNumber
        police_station_details.save()
        details = True
        print("E")

        station_address = PoliceStationAddress()
        station_address.pId = pId
        station_address.street = street
        station_address.city = city
        station_address.state = state
        print("HH")
        if country is not None: station_address.country = country
        station_address.zip_code = zip_code
        station_address.zone = zone
        print("HHH")
        station_address.save()
        print("GGGG")
        address = True
        print("F")
    
    except:
        print("G")
        if login:
            police_login = PoliceLogin.objects(pId=pId).first().delete()
        
        if details:
            police_station_details = PoliceStationDetails.objects(pId=pId).first().delete()
        
        if address:
            station_address = PoliceStationAddress.objects(pId=pId).first().delete()

        registrationStatus = False
        message = 'Error'
        
    
    registration_info['registrationStatus'] = registrationStatus
    registration_info['message'] = message

def registration(registration_info):
    pId = registration_info['pId']
    police = PoliceLogin.objects(pId=pId)
    # police = []
    registration_info['registrationStatus'] = None
    registration_info['message'] = None

    if len(police):
        registration_info['registrationStatus'] = False
        registration_info['message'] = 'Account Exist'

    else:
        create_account(registration_info=registration_info)
    
    return registration_info

