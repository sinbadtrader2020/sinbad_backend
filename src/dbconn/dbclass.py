class DBAbstract:
    def get_key_value_format(self):
        str_keys = ''
        values = list()
        str_format = ''
        for attr, value in self.__dict__.items():
            if value is not None:
                if str_keys:
                    str_keys += ', '
                    str_format += ', '

                str_keys += attr
                values.append(value)
                str_format += '%s'

        return str_keys, values, str_format


class User(DBAbstract):
    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 email=None,
                 mobile_number=None,
                 password=None,
                 street_address=None,
                 city=None,
                 country=None,
                 zip_code=None,
                 language=None,
                 user_create=None,
                 status=None,
                 **kwargs):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_number = mobile_number
        self.password = password
        self.street_address=street_address
        self.city = city
        self.country = country
        self.zip_code=zip_code
        self.language = language
        self.user_create = user_create
        self.status = status