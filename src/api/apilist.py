from src.api.logout import Logout
from src.api.user import User, UserList


apis = {
    '/logout'           : Logout,

    '/user'             : UserList,
    '/user/<int:id>'    : User
}