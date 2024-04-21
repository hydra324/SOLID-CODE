# requirements:
# 1. different locker sizes - like small, medium and large
# 2. locker is assigned to customer based on package size
# 3. returns should be supported
# 4. when order is delivered or to be returned an OTP should be sent to customer
# 5. there's also a delivery guy and almost the same rules apply to him
# 6. if customer doesnt pick up within x amount of days, refund will be initiated
# 7. one locker location has multiple lockers
# 8. customer can choose which location to pickup from / drop at
# 9. locker should have states like closed / open

from enum import Enum

class LockerSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class LockerState(Enum):
    CLOSED = 1 # booked and a package is inside
    OPEN = 2 # booked and ready to add package
    AVAILABLE = 3 # free to be booked
    BOOKED = 4 # pakcage not placed yet

class Item:
    def __init__(self,item_id,quantity) -> None:
        self.__item_id = item_id
        self.__quantity = quantity

    def get_item(self):
        return self.__item_id

class Order:
    def __init__(self,order_id,items: list[Item],delivery_location) -> None:
        self.__order_id = order_id
        self.__items = items
        self.delivery_location = delivery_location

class Package:
    def __init__(self, package_id,package_size,order:Order) -> None:
        self.__package_id = package_id
        self.package_size = package_size
        self.order = order

class LockerPackage(Package):
    def __init__(self, package_id, package_size, order: Order, code_valid_days, code, package_deliery_time, locker_id) -> None:
        
        self.__code_valid_days = code_valid_days
        self.__code = code
        self.__package_delivery_time = package_deliery_time
        self.__locker_id = locker_id
        super().__init__(package_id, package_size, order)

    def __is_valid_code(self,code) -> bool:
        return code==self.__code
    
    def verify_code(self,code,time):
        return self.__is_valid_code(code) and time-self.__package_delivery_time <= self.__code_valid_days
    
class Locker:
    def __init__(self,locker_id,locker_size: LockerSize,location_id,locker_state:LockerState = LockerState.AVAILABLE) -> None:
        self.__locker_id = locker_id
        self.__locker_size = locker_size
        self.__location_id = location_id
        self.__locker_state = locker_state

    def add_package(self,pakcage:LockerPackage) -> None :
        if self.__locker_state!=LockerState.OPEN:
            raise ValueError(f"Locker state is {self.__locker_state} and thus package cannot be placed")
        pass

class LockerLocation:
    def __init__(self, name, lockers, longitude, latitude, open_time, close_time):
        self.__name = name
        self.__lockers = lockers # list of lockers
        self.__longitude = longitude
        self.__latitude = latitude 
        self.__open_time = open_time
        self.__close_time = close_time

# singelton instance
# class __LockerService(object):
#     __instances = None

#     def __new__(cls):
#         if cls.__instances is None:
#             cls.__instances = super(__LockerService, cls).__new__(cls)
#         return cls.__instances
    
# class LockerService(metaclass=__LockerService):
#     def __init__(self) -> None:
#         self.__locations = {}

class LockerService(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating singleton instance')
            cls._instance = super(LockerService, cls).__new__(cls)
            cls._instance.__locations = {'loc1':'austin'}
        return cls._instance
    
    def get_locations(cls):
        return cls._instance.__locations
    
    def set_locations(cls,locations):
        cls._instance.__locations = locations 


class Notification:
    def __init__(self,customer_id,order_id,locker_id,code) -> None:
        self.__customer_id = customer_id
        self.__order_id = order_id
        self.__locker_id = locker_id
        self.__code = code
    def send(self):
        # send notification
        pass

ls = LockerService()
print(ls.get_locations())
ls1 = LockerService()
ls1.set_locations({'loc2':'dallas'})
print(ls.get_locations())
print(ls1.get_locations())
print(LockerService().get_locations())


# sample singleton class

class MyClass(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MyClass,cls).__new__(cls)
            # any initializations
            cls.__instance.__member_variable = 'some val'
        return cls.__instance
    
    def get_member_variable(cls):
        return cls.__instance.__member_variable