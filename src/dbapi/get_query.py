from src.dbconn import query, dbname
from src.config import ApiConfig, UserConfig, CompanyConfig, CompliantConfig


def get_all_user():
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW, group=True)
    return result, success


def get_user_by_id(id):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW,
                                     field_name=ApiConfig.ID,
                                     field_value=id)
    return result, success


def get_user_by_email(email):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE,
                                     field_name=UserConfig.EMAIL,
                                     field_value=email)
    return result, success


def get_user_by_email_view(email):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW,
                                     field_name=UserConfig.EMAIL,
                                     field_value=email)
    return result, success


def get_company_details(symbol=None, limit='ALL', offset=0):
    result= {}
    success = False
    if symbol==None:
        if limit == 0:
            limit = 'ALL'
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY, limit=limit,
                                               offset=offset, group=True)
    else:
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY,
                                           field_name=CompanyConfig.ACT_SYMBOL,
                                           field_value=symbol)
    return result, success


def get_compliant_type_company_details(compliant_type=CompliantConfig.COMPLIANT, symbol=None,
                                       limit='ALL', offset=0):
    result= {}
    success = False
    if symbol==None:
        if limit == 0:
            limit = 'ALL'
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY_VIEW,
                                           limit=limit, offset=offset,
                                           field_name=CompanyConfig.AAOIFI_COMPLIANT,
                                           field_value=compliant_type)
    else:
        field_name = [CompanyConfig.AAOIFI_COMPLIANT, CompanyConfig.ACT_SYMBOL]
        field_value = [compliant_type, symbol]
        result, success = query.get_record(table_name=dbname.DBClassName.COMPANY_VIEW,
                                           field_name=field_name,
                                           field_value=field_value, qparam=True)
    return result, success


def get_company_number(compliant_type=None):

    if compliant_type == None:
        result, success = query.get_count(dbname.DBClassName.COMPANY)
    else:
        result, success = query.get_count_item_wise(table_name=dbname.DBClassName.COMPANY,
                                           field_name=CompanyConfig.AAOIFI_COMPLIANT,
                                           field_value=compliant_type)
    return result, success


def company_search(id):
    field_name = [CompanyConfig.COMPANY_NAME, CompanyConfig.ACT_SYMBOL]
    field_value = [id, id]

    result, success = query.item_search(table_name=dbname.DBClassName.COMPANY,
                                       field_name=field_name,
                                       field_value=field_value)
    return result, success
