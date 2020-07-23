import memcache


memclient = None
abc = False

def connectmemcached():
    global abc
    if abc == False:
        print("connect memcached===>")
        memclient = memcache.Client(['127.0.0.1:11211'], debug=0)
        print(memclient)
        abc = True


def setvalue(key=None, value=None, time=43200):
    if key is None or value is None:
        return False

    return memclient.set(key, value, time=time)

def getvalue(key=None):
    if key is None:
        return None

    return memclient.get(key)


def deletevalue(key=None):
    if key is None:
        return False

    return memclient.delete(key)


def clearmemcache():
    memclient.clear()


