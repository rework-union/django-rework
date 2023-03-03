from rest_framework.views import exception_handler as rest_framework_exception_handler


def exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = rest_framework_exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = exc.get_codes()
        response.data['detail'] = str(exc.detail)
        if exc.errors:
            response.data['errors'] = exc.errors

    return response
