# Source: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# List of HTTP status codes

###############################################################################
# 1xx Informational
###############################################################################

HTTP_CONTINUE = 100
HTTP_SWITCHING_PROTOCOLS = 101
HTTP_PROCESSING = 102  # WebDAV
HTTP_EARLY_HINTS = 103

###############################################################################
# 2xx Success
###############################################################################

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_NO_CONTENT = 204
HTTP_RESET_CONTENT = 205
HTTP_PARTIAL_CONTENT = 206
HTTP_MULTI_STATUS = 207  # WebDAV
HTTP_ALREADY_REPORTED = 208  # WebDAV
HTTP_IM_USED = 226

###############################################################################
# 3xx Redirection
###############################################################################

HTTP_MULTIPLE_CHOICES = 300
HTTP_MOVED_PERMANENTLY = 301
HTTP_FOUND = 302
HTTP_SEE_OTHER = 303
HTTP_NOT_MODIFIED = 304
HTTP_USE_PROXY = 305
HTTP_SWITCH_PROXY = 306
HTTP_TEMPORARY_REDIRECT = 307
HTTP_RESUME_INCOMPLETE = 308

###############################################################################
# 4xx Client Error
###############################################################################

HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_PAYMENT_REQUIRED = 402
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_NOT_ACCEPTABLE = 406
HTTP_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_REQUEST_TIMEOUT = 408
HTTP_CONFLICT = 409
HTTP_GONE = 410
HTTP_LENGTH_REQUIRED = 411
HTTP_PRECONDITION_FAILED = 412
HTTP_PAYLOAD_TOO_LARGE = 413
HTTP_URI_TOO_LONG = 414
HTTP_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_RANGE_NOT_SATISFIABLE = 416
HTTP_EXPECTATION_FAILED = 417
HTTP_IM_A_TEAPOT = 418
HTTP_MISDIRECTED_REQUEST = 421
HTTP_UNPROCESSABLE_ENTITY = 422  # WebDAV
HTTP_LOCKED = 423  # WebDAV
HTTP_FAILED_DEPENDENCY = 424  # WebDAV
HTTP_UNORDERED_COLLECTION = 425
HTTP_UPGRADE_REQUIED = 426
HTTP_PRECONDITION_REQUIRED = 428
HTTP_TOO_MANY_REQUESTS = 429
HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_NO_RESPONSE = 444
HTTP_RETRY_WITH = 449
HTTP_BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS = 450
HTTP_UNAVAILABLE_FOR_LEGAL_REASONS = 451
HTTP_CLIENT_CLOSED_REQUEST = 499

###############################################################################
# 5xx Server Error
###############################################################################

HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_NOT_IMPLEMENTED = 501
HTTP_BAD_GATEWAY = 502
HTTP_SERVICE_UNAVAILABLE = 503
HTTP_GATEWAY_TIMEOUT = 504
HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_VARIANT_ALSO_NEGOTIATES = 506
HTTP_INSUFFICIENT_STORAGE = 507  # WebDAV
HTTP_LOOP_DETECTED = 508  # WebDAV
HTTP_BANDWIDTH_LIMIT_EXCEEDED = 509
HTTP_NOT_EXTENDED = 510
HTTP_NETWORK_AUTHENTICATION_REQUIRED = 511
HTTP_NETWORK_READ_TIMEOUT_ERROR = 598  # not used in RFC
HTTP_NETWORK_CONNECT_TIMEOUT_ERROR = 599  # not used in RFC

# List of HTTP status Messages

_status = dict()

###############################################################################
# 1xx Informational
###############################################################################

_status[HTTP_CONTINUE] = "Continue"
_status[HTTP_SWITCHING_PROTOCOLS] = "Switching Protocols"
_status[HTTP_PROCESSING] = "Processing"  # WebDAV
_status[HTTP_EARLY_HINTS] = "Early Hints"

###############################################################################
# 2xx Success
###############################################################################

_status[HTTP_OK] = "OK"
_status[HTTP_CREATED] = "Created"
_status[HTTP_ACCEPTED] = "Accepted"
_status[HTTP_NON_AUTHORITATIVE_INFORMATION] = "Non-Authoritative Information"
_status[HTTP_NO_CONTENT] = "No Content"
_status[HTTP_RESET_CONTENT] = "Reset Content"
_status[HTTP_PARTIAL_CONTENT] = "Partial Content"
_status[HTTP_MULTI_STATUS] = "Multi-Status"  # WebDAV
_status[HTTP_ALREADY_REPORTED] = "Already Reported"  # WebDAV
_status[HTTP_IM_USED] = "IM Used"

###############################################################################
# 3xx Redirection
###############################################################################

_status[HTTP_MULTIPLE_CHOICES] = "Multiple Choices"
_status[HTTP_MOVED_PERMANENTLY] = "Moved Permanently"
_status[HTTP_FOUND] = "Found"
_status[HTTP_SEE_OTHER] = "See Other"
_status[HTTP_NOT_MODIFIED] = "Not Modified"
_status[HTTP_USE_PROXY] = "Use Proxy"
_status[HTTP_SWITCH_PROXY] = "Switch Proxy"
_status[HTTP_TEMPORARY_REDIRECT] = "Temporary Redirect"
_status[HTTP_RESUME_INCOMPLETE] = "Permanent Redirect"

###############################################################################
# 4xx Client Error
###############################################################################

_status[HTTP_BAD_REQUEST] = "Bad Request"
_status[HTTP_UNAUTHORIZED] = "Unauthorized"
_status[HTTP_PAYMENT_REQUIRED] = "Payment Required"
_status[HTTP_FORBIDDEN] = "Forbidden"
_status[HTTP_NOT_FOUND] = "Not Found"
_status[HTTP_METHOD_NOT_ALLOWED] = "Method Not Allowed"
_status[HTTP_NOT_ACCEPTABLE] = "Not Acceptable"
_status[HTTP_PROXY_AUTHENTICATION_REQUIRED] = "Proxy Authentication Required"
_status[HTTP_REQUEST_TIMEOUT] = "Request Timeout"
_status[HTTP_CONFLICT] = "Conflict"
_status[HTTP_GONE] = "Gone"
_status[HTTP_LENGTH_REQUIRED] = "Length Required"
_status[HTTP_PRECONDITION_FAILED] = "Precondition Failed"
_status[HTTP_PAYLOAD_TOO_LARGE] = "Payload Too Large"
_status[HTTP_URI_TOO_LONG] = "URI Too Long"
_status[HTTP_UNSUPPORTED_MEDIA_TYPE] = "Unsupported Media Type"
_status[HTTP_RANGE_NOT_SATISFIABLE] = "Range Not Satisfiable"
_status[HTTP_EXPECTATION_FAILED] = "Expectation Failed"
_status[HTTP_IM_A_TEAPOT] = "I'm a teapot"
_status[HTTP_MISDIRECTED_REQUEST] = "Misdirected Request"
_status[HTTP_UNPROCESSABLE_ENTITY] = "Unprocessable Entity"  # WebDAV
_status[HTTP_LOCKED] = "Locked"  # WebDAV
_status[HTTP_FAILED_DEPENDENCY] = "Failed Dependency"  # WebDAV
_status[HTTP_UNORDERED_COLLECTION] = "Unordered Collection"
_status[HTTP_UPGRADE_REQUIED] = "Upgrade Required"
_status[HTTP_PRECONDITION_REQUIRED] = "Precondition Required"
_status[HTTP_TOO_MANY_REQUESTS] = "Too Many Requests"
_status[HTTP_REQUEST_HEADER_FIELDS_TOO_LARGE] = "Request Header Fields Too Large"
_status[HTTP_NO_RESPONSE] = ""
_status[HTTP_RETRY_WITH] = ""
_status[HTTP_BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS] = ""
_status[HTTP_UNAVAILABLE_FOR_LEGAL_REASONS] = "Unavailable For Legal Reasons"
_status[HTTP_CLIENT_CLOSED_REQUEST] = "Client Closed Request"  # A non-standard status code introduced by nginx

###############################################################################
# 5xx Server Error
###############################################################################

_status[HTTP_INTERNAL_SERVER_ERROR] = "Internal Server Error"
_status[HTTP_NOT_IMPLEMENTED] = "Not Implemented"
_status[HTTP_BAD_GATEWAY] = "Bad Gateway"
_status[HTTP_SERVICE_UNAVAILABLE] = "Service Unavailable"
_status[HTTP_GATEWAY_TIMEOUT] = "Gateway Timeout"
_status[HTTP_VERSION_NOT_SUPPORTED] = "HTTP Version Not Supported"
_status[HTTP_VARIANT_ALSO_NEGOTIATES] = "Variant Also Negotiates"
_status[HTTP_INSUFFICIENT_STORAGE] = " Insufficient Storage"  # WebDAV
_status[HTTP_LOOP_DETECTED] = "Loop Detected"  # WebDAV
_status[HTTP_BANDWIDTH_LIMIT_EXCEEDED] = "Bandwidth Limit Exceeded"  # not used in RFC
_status[HTTP_NOT_EXTENDED] = "Not Extended"
_status[HTTP_NETWORK_AUTHENTICATION_REQUIRED] = "Network Authentication Required"
_status[HTTP_NETWORK_READ_TIMEOUT_ERROR] = "Network read timeout error"  # not used in RFC
_status[HTTP_NETWORK_CONNECT_TIMEOUT_ERROR] = "Network Connect Timeout Error"  # not used in RFC


def get_status_code(status):
    return str(status) + " " + _status[status]


def get_status_message(status):
    return _status[status]


GET = 1
HEAD = 2
POST = 3
PUT = 4
DELETE = 5
CONNECT = 6
OPTIONS = 7
TRACE = 8
PATCH = 9

_RESPONSE = dict()

from flask import jsonify, make_response, abort
from src.config import ApiConfig
from psycopg2 import errorcodes
from src.http.errormessage import error_types, error_names


def get_error_message(error):
    error_type = None
    error_name = None
    error_msg = str(error)
    for key in error_types:
        if key == errorcodes.lookup(error.pgcode):
            error_type = error_types[key]

    for key in error_names:
        if key in error_msg:
            error_name = error_names[key]

    return error_name + " " + error_type, errorcodes.lookup(error.pgcode)


def _make_gpd_response(data, success, **kwargs):
    status_code = HTTP_OK  # get_status_code(HTTP_OK)
    if success:
        if not data[ApiConfig.DATA]:
            status_code = HTTP_NO_CONTENT  # get_status_code(HTTP_NO_CONTENT)
    else:
        # status_code = get_status_code(HTTP_UNPROCESSABLE_ENTITY)
        status_code = HTTP_BAD_REQUEST
        if ApiConfig.MESSAGE not in data:
            abort(HTTP_UNPROCESSABLE_ENTITY, data[ApiConfig.ERROR])
        else:
            data = {ApiConfig.ERROR: "MISSING REQUIRED ITEM", ApiConfig.MESSAGE: data[ApiConfig.MESSAGE]}

    return make_response(jsonify(data), status_code)


def _make_pp_response(data, success, **kwargs):
    status_code = HTTP_CREATED  # get_status_code(HTTP_CREATED)
    if not success:
        # status_code = get_status_code(HTTP_UNPROCESSABLE_ENTITY)
        status_code = HTTP_BAD_REQUEST
        if ApiConfig.MESSAGE not in data:
            error_msg, error = get_error_message(data[ApiConfig.ERROR])
            if error_msg is not None:
                data = {ApiConfig.ERROR: error, ApiConfig.MESSAGE: error_msg}
            else:
                abort(HTTP_UNPROCESSABLE_ENTITY, data[ApiConfig.ERROR])
        else:
            data = {ApiConfig.ERROR: "MISSING REQUIRED ITEM", ApiConfig.MESSAGE: data[ApiConfig.MESSAGE]}
    return make_response(jsonify(data), status_code)


_RESPONSE[GET] = _make_gpd_response
_RESPONSE[PUT] = _make_pp_response
_RESPONSE[DELETE] = _make_gpd_response
_RESPONSE[POST] = _make_pp_response


def get_response(data, success, method):
    return _RESPONSE[method](data, success)
