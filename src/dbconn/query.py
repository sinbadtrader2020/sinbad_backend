from src.dbconn.connection import connection
from src.config import ApiConfig


def _execute_select(sql, data=None):
    success = False
    try:
        with connection.get_db_cursor() as cursor:
            if data:
                cursor.execute(sql, data)
            else:
                cursor.execute(sql)
            rows = cursor.fetchall()
            result = {ApiConfig.DATA: rows}
            success = True
    except Exception as e:
        print(e)
        result = {ApiConfig.ERROR: str(e)}

    return result, success


def _execute_iud(sql, data, commit=False):
    success = False
    result = ''
    try:
        with connection.get_db_cursor(commit) as cursor:
            print(cursor.mogrify(sql, data))
            cursor.execute(sql, data)
            rows = cursor.fetchall()
            result = {ApiConfig.DATA: rows}
            success = True
    except Exception as e:
        print(e)
        # print(e.__dict__)
        # print(e.pgcode)
        # print(errorcodes.lookup(e.pgcode[:2]))
        # print(errorcodes.lookup(e.pgcode))
        result = {ApiConfig.ERROR: e}

    return result, success


def get_record(table_name=None, group=False, offset=0, limit='ALL', field_name=None, qparam=False):
    data = None
    if group:
        sql = """SELECT * from {0} LIMIT {1} OFFSET {2}""".format(table_name, limit, offset)
    elif qparam:
        tmp = """SELECT * from {0} WHERE {1} = %s"""
        for i in range(1, len(field_name)):
            tmp += """ and {""" + str(i+1) + """} = %s"""

        sql = tmp.format(table_name, *field_name)
        data = offset
    else:
        sql = """SELECT * from {0} WHERE {1} = %s""".format(table_name, field_name)
        data = (offset,)

    print(sql)
    return _execute_select(sql, data)


def login_query(table_name=None, offset=0, field_name=None):
    data = None

    sql = """SELECT * from {0} WHERE {1} = %s and {2} = %s""".format(table_name, field_name[0], field_name[1])

    data = (offset[0], offset[1],)
    return _execute_select(sql, data)

# [ApiConfig.EMPLOYEE_EMAIL, ApiConfig.EMPLOYEE_PASSWORD, ApiConfig.EMPLOYEE_NEW_PASSWORD, ApiConfig.EMPLOYEE_ID]
def change_password(table_name=None, offset=0, field_name=None):
    data = None
    sql = """update {0} set {1} = %s WHERE {2} = %s and {3} = %s RETURNING {4}""".format(table_name, field_name[1], field_name[0],
                                                                            field_name[1], field_name[2])

    data = offset
    return _execute_iud(sql, data, commit=True)


def reset_password(emp_id=None, new_password=None):
    data = None
    sql = """UPDATE pr_employee SET emp_password = %s WHERE emp_id = %s RETURNING emp_id;"""
    data = [new_password, emp_id]
    return _execute_iud(sql, data, commit=True)


def get_count(table_name=None):
    sql = """SELECT COUNT(*) FROM {0}""".format(table_name)

    return _execute_select(sql)


def create_record(table_name=None, record=None, field_name=None, production=True):
    str_keys, values, str_format = record.get_key_value_format()
    sql = """INSERT INTO {0} ({1}) VALUES ({2}) RETURNING {3}""" \
        .format(table_name, str_keys, str_format, field_name)
    print(sql)

    return _execute_iud(sql, values, commit=production)


def update_record(table_name=None, record=None, field_name=None, field_value=None, production=True):
    str_keys, values, str_format = record.get_key_value_format()
    if len(values) > 1:
        sql = """UPDATE {0} SET ({1}) = ({2}) WHERE {3} = %s RETURNING {4}""" \
            .format(table_name, str_keys, str_format, field_name, field_name)
    else:
        sql = """UPDATE {0} SET {1} = {2} WHERE {3} = %s RETURNING {4}""" \
            .format(table_name, str_keys, str_format, field_name, field_name)
    values.append(field_value)
    return _execute_iud(sql, values, commit=production)

