from src.api.logout import Logout
from src.api.user import User, UserList
from src.api.password import ResetPassword, ForgetPassword
from src.api.company import Company, CompanyList


apis = {
    '/logout'               : Logout,

    '/user'                 : UserList,
    '/user/<int:id>'        : User,

    '/resetpassword'        : ResetPassword,
    '/forgetpassword'       : ForgetPassword,
    
    '/company'              : CompanyList,
    '/company/<string:id>'  : Company
}