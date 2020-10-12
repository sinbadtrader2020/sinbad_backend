from src.api.logout import Logout
from src.api.user import User, UserList
from src.api.password import ResetPassword, ForgetPassword
from src.api.company import Company, CompanyList, CompliantCompany, \
    CompliantCompanyList, NonCompliantCompany, NonCompliantCompanyList, YellowCompany, YellowCompanyList


apis = {
    '/logout'               : Logout,

    '/user'                 : UserList,
    '/user/<int:id>'        : User,

    '/resetpassword'        : ResetPassword,
    '/forgetpassword'       : ForgetPassword,
    
    '/company'              : CompanyList,
    '/company/<string:id>'  : Company,
    '/company/compliant'                    : CompliantCompanyList,
    '/company/compliant/<string:id>'        : CompliantCompany,
    '/company/noncompliant'                 : NonCompliantCompanyList,
    '/company/noncompliant/<string:id>'     : NonCompliantCompany,
    '/company/yellow'                       : YellowCompanyList,
    '/company/yellow/<string:id>'           : YellowCompany
}