# COM2042-Django-Web-Apps
This repo tracks my progress of learning Django Web Framework as part of my course degree

## App creation

First, I created my project using the following command:

```bash
python3 -m django startproject lab01
cd ./lab01
```

Following the creation of the project, I created my first app within it called 'inspector' with the following bash command. When the project is created, change to the project directory and after that to create an app use manage.py script along with startapp and the name of the app.

```bash
python3 manage.py startapp <name of the app>

In my case is:
python3 manage.py startapp inspector
``` 

I implemented two views to display simple 'Hello world!' and custom message given from query parameters or as headers when HTTP Get Request is sent. The headers overwrite the parameters.

```python
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
```

Then in order for the view to function it needs to be connected to a path. ***hello*** view is connected to ***hello/***

```python
path('hello/', views.hello)
```

***inspector*** view:

```python
path('inspect/', views.inspect)
```