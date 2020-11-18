###### PLACEHOLDER ######
# Client Data Structure #
#########################


class ClientInformation:
    def __init__(self, title, fname, lname, address, dob):
        self.__title = title
        self.__first_name = fname
        self.__last_name = lname
        self.__address = address
        self.__date_of_birth = dob

    @property
    def title(self):
        return self.__title

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def address(self):
        return self.__address

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def full_name(self):
        return f"{self.__title} {self.__first_name} {self.__last_name}"
