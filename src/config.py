class ApiConfig:
    ADMIN               = 'admin'
    ADMIN_PASSWORD      = 'ADMIN_PASSWORD'
    REST_URL_PREFIX     = 'REST_URL_PREFIX'
    API_VERSION         = 'API_VERSION'
    DATA                = 'data'
    ERROR               = 'error'
    MESSAGE             = 'message'
    ID                  = 'id'
    TOKEN               = 'token'
    RESET_PASSWORD      = '0123456789'
    LIMIT               = 'limit'
    OFFSET              = 'offset'
    NEXT_OFFSET         = 'next_offset'
    TOTAL_ITEM          = 'total_item'
    COUNT               = 'count'


class APIMethod:
    POST    = 'POST'
    PUT     = 'PUT'
    GET     = 'GET'
    DELETE  = 'DELETE'


class Status:
    Status      = 'status'
    Active      = 'ACTIVE'
    Inactive    = 'INACTIVE'


class UserConfig:
    FIRSTNAME       = 'first_name'
    LASTNAME        = 'last_name'
    EMAIL           = 'email'
    CITY            = 'city'
    COUNTRY         = 'country'
    MOBILE_NUMBER   = 'mobile_number'
    LANGUAGE        = 'language'
    PASSWORD        = 'password'
    USERCREATETIME  = 'user_create'
    NEW_PASSWORD    = 'new_password'
    VERIFY_CODE     = 'verifycode'


class CompanyConfig:
    ACT_SYMBOL      = 'sf_act_symbol'
    COMPANY_NAME    = 'sf_company_name'
    SECURITY_NAME   = 'sf_security_name'
    EXCHANGE        = 'sf_exchange'
    CQS_SYMBOL      = 'sf_cqs_symbol'
    ETF             = 'sf_etf'
    ROUND_LOT_SIZE  = 'sf_round_lot_size'
    TEST_ISSUE      = 'sf_test_issue'
    NASDAQ_SYMBOL   = 'sf_nasdaq_symbol'
    LAST_SCREENED   = 'sf_last_screened'
    AAOIFI_COMPLIANT    = 'sf_aaoifi_compliant'
    NC_REASON       = 'sf_nc_reason'


class CompliantConfig:
    COMPLIANT           = 'COMPLIANT',
    NONCOMPLIANT        = 'NON-COMPLIANT',
    YELLOW              = 'YELLOW'


class MAILConfig:
    SENDER              = 'marufcuet007@gmail.com'
