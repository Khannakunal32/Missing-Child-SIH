'''from src.models.child_database import ChildInfo
from src.models.child_database import ChildInformantInfo
from src.models.child_database import ChildFaceEncoding

def missing_child_database():
    missing_childs = ChildFaceEncoding.objects(isFound=False).as_pymongo()
    numbers_of_missing_child = len(missing_childs)
    missing_child_details = {
        'isFound': False,
        'quantity': numbers_of_missing_child,
        'details': list()
    }

    for i in range(numbers_of_missing_child):
        curChild = dict()
        cId = numbers_of_missing_child[i].cId
        child_detail_length = ChildInfo.objects(cId=cId)
        if len(child_detail_length):
            child_detail = child_detail_length.first()
            curChild['firstName'] = child_detail.firstName
            try:
                curChild['middleName'] = child_detail.middleName
            except:
                pass
            try:
                curChild['lastName'] = child_detail.lastName
            except:
                pass
            curChild['fir_no'] = child_detail.fir_no
            curChild['gender'] = child_detail.gender
            try:
                curChild['dob'] = child_detail.dob
            except:
                pass
            try:
                curChild['age'] = child_detail.age
            except:
                pass
            try:
                curChild['date_of_missing'] = child_detail.date_of_missing
            except:
                pass
            try:
                curChild['place_of_missing'] = child_detail.place_of_missing
            except:
                pass
            try:
                curChild['color'] = child_detail.color
            except:
                pass
            try:
                curChild['hairColour'] = child_detail.hairColour
            except:
                pass
            try:
                curChild['imageURL'] = child_detail.imageURL
            except:
                pass
        
        child_guardian_detail_length = ChildGuardianInfo.objects(cId=cId)
        if len(child_guardian_detail_length):
            child_guardian_detail = child_detail_length.first()
            try:
                curChild['guardianName'] = child_guardian_detail.guardianName
            except:
                pass
            try:
                curChild['guardianEmailId'] = child_guardian_detail.guardianEmailId
            except:
                pass
            try:
                curChild['guardianPhoneNumber'] = child_guardian_detail.guardianPhoneNumber
            except:
                pass
            try:
                curChild['guardianAddress'] = child_guardian_detail.guardianAddress
            except:
                pass
        
        missing_child_details['details'].append(curChild)
    
    return missing_child_details

def found_child_database():
    found_childs = ChildFaceEncoding.objects(isFound=True).as_pymongo()
    numbers_of_found_child = len(found_childs)
    found_child_details = {
        'isFound': True,
        'quantity': numbers_of_found_child,
        'details': list()
    }

    for i in range(numbers_of_found_child):
        curChild = dict()
        cId = numbers_of_found_child[i].cId
        child_detail_length = ChildInfo.objects(cId=cId)
        if len(child_detail_length):
            child_detail = child_detail_length.first()
            curChild['firstName'] = child_detail.firstName
            try:
                curChild['middleName'] = child_detail.middleName
            except:
                pass
            try:
                curChild['lastName'] = child_detail.lastName
            except:
                pass
            curChild['fir_no'] = child_detail.fir_no
            curChild['gender'] = child_detail.gender
            try:
                curChild['dob'] = child_detail.dob
            except:
                pass
            try:
                curChild['age'] = child_detail.age
            except:
                pass
            try:
                curChild['date_of_missing'] = child_detail.date_of_missing
            except:
                pass
            try:
                curChild['place_of_missing'] = child_detail.place_of_missing
            except:
                pass
            try:
                curChild['color'] = child_detail.color
            except:
                pass
            try:
                curChild['hairColour'] = child_detail.hairColour
            except:
                pass
            try:
                curChild['imageURL'] = child_detail.imageURL
            except:
                pass
        
        child_guardian_detail = ChildGuardianInfo.objects(cId=cId)
        if len(child_guardian_detail):
            child_guardian_detail = child_guardian_detail.first()
            try:
                curChild['guardianName'] = child_guardian_detail.guardianName
            except:
                pass
            try:
                curChild['guardianEmailId'] = child_guardian_detail.guardianEmailId
            except:
                pass
            try:
                curChild['guardianPhoneNumber'] = child_guardian_detail.guardianPhoneNumber
            except:
                pass
            try:
                curChild['guardianAddress'] = child_guardian_detail.guardianAddress
            except:
                pass
        
        found_child_details['details'].append(curChild)
    
    return found_child_details

def get_child_details(cId):
    curChild = dict()
    child_info = ChildInfo.objects(cId=cId)

    if len(child_info):
        child_detail = child_info.first().as_pymongo()
        curChild['firstName'] = child_detail.firstName
        try:
            curChild['middleName'] = child_detail.middleName
        except:
            pass
        try:
            curChild['lastName'] = child_detail.lastName
        except:
            pass
        curChild['fir_no'] = child_detail.fir_no
        curChild['gender'] = child_detail.gender
        try:
            curChild['dob'] = child_detail.dob
        except:
            pass
        try:
            curChild['age'] = child_detail.age
        except:
            pass
        try:
            curChild['date_of_missing'] = child_detail.date_of_missing
        except:
            pass
        try:
            curChild['place_of_missing'] = child_detail.place_of_missing
        except:
            pass
        try:
            curChild['color'] = child_detail.color
        except:
            pass
        try:
            curChild['hairColour'] = child_detail.hairColour
        except:
            pass
        try:
            curChild['imageURL'] = child_detail.imageURL
        except:
            pass
    
    child_guardian_detail= ChildGuardianInfo.objects(cId=cId)
    if len(child_guardian_detail):
        child_guardian_detail = child_guardian_detail.first()
        try:
            curChild['guardianName'] = child_guardian_detail.guardianName
        except:
            pass
        try:
            curChild['guardianEmailId'] = child_guardian_detail.guardianEmailId
        except:
            pass
        try:
            curChild['guardianPhoneNumber'] = child_guardian_detail.guardianPhoneNumber
        except:
            pass
        try:
            curChild['guardianAddress'] = child_guardian_detail.guardianAddress
        except:
            pass
    
    return curChild

       ''' 

