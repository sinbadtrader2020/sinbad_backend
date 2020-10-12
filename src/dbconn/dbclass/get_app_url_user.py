from src.dbconn.dbabstract import DBAbstract


class SubscribeUser(DBAbstract):
    def __init__(self,
                 id=None,
                 mobile_number=None,
                 created=None,
                 **kwargs):
        self.id = id
        self.mobile_number = mobile_number
        self.created = created