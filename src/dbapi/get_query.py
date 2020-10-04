from src.dbconn import query, dbname
from src.config import ApiConfig, UserConfig, CompanyConfig


def get_all_user():
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW, group=True)
    return result, success


def get_user_by_id(id):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW,
                                     field_name=ApiConfig.ID,
                                     offset=id)
    return result, success


def get_user_by_email(email):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE,
                                     field_name=UserConfig.EMAIL,
                                     offset=email)
    return result, success


def get_user_by_email_view(email):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW,
                                     field_name=UserConfig.EMAIL,
                                     offset=email)
    return result, success


def get_company_details(symbol=None):
    result= {}
    success = False
    if symbol==None:
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY, group=True)
    else:
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY,
                                           field_name=CompanyConfig.ACT_SYMBOL,
                                           offset=symbol)
    return result, success


def get_compliant_company_details(symbol=None):
    result= {}
    success = False
    if symbol==None:
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY,
                                           field_name=CompanyConfig.AAOIFI_COMPLIANT,
                                           offset=True)
    else:
        field_name = [CompanyConfig.AAOIFI_COMPLIANT, CompanyConfig.ACT_SYMBOL]
        offset = [True, symbol]
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY,
                                           field_name=field_name,
                                           offset=offset, qparam=True)
    return result, success