
class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

        def get_name(self):
            return self.__name

        def get_address(self):
            return self.__address

        def get_phone(self):
            return self.__phone

        def print_person(self):
            print('Method 1')
            print('Name:', self.__name)
            print('Addr:', self.__address)
            print('Phone:',self.__phone)

            print()
            print()

            print('Method 2')
            Person.print_person_self

            print('Customer number:', self.__cust_number)
            if self.__on_list:
                print('On mailing list: Yes')
            else:
                print('On mailing list: No')



