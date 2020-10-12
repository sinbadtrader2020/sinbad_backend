from src.dbconn.dbabstract import DBAbstract


class SubscribeUser(DBAbstract):
    def __init__(self,
                 id=None,
                 name=None,
                 email=None,
                 subscribe_status=None,
                 created=None,
                 updated=None,
                 **kwargs):
        self.id = id
        self.name = name
        self.email = email
        self.subscribe_status = subscribe_status
        self.created = created
        self.updated = updated