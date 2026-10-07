from django.http import HttpResponse

# Create your views here.


def hello(request):
    message = request.GET.get('message', 'Hello world!')
    message = request.headers.get('Lab-Message', message)
    return HttpResponse(message)


def inspect(request):
    request_method = request.method
    path = request.get_full_path()
    request_headers = request.headers
    parameters = request.GET

    result = f'Method: {request_method} Path: {path}\n'

    for header in request_headers.keys():
        result += f'{header}: {request_headers.get(header)}'
        result += '\n'

    for param in parameters.keys():
        result += f'{param}: {parameters.get(param)}'
        result += '\n'

    return HttpResponse(result, content_type='text/plain')
