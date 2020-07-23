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
                 city=None,
                 country=None,
                 mobile_number=None,
                 language=None,
                 password=None,
                 user_create=None,
                 status=None,
                 **kwargs):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city
        self.country = country
        self.mobile_number = mobile_number
        self.language = language
        self.password = password
        self.user_create = user_create
        self.status = status