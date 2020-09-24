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