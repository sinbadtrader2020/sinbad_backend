from src.api.logout import Logout
from src.api.user import User, UserList
from src.api.company import Company, CompanyList


apis = {
    '/logout'               : Logout,

    '/user'                 : UserList,
    '/user/<int:id>'        : User,
    
    '/company'              : CompanyList,
    '/company/<string:id>'  : Company
}