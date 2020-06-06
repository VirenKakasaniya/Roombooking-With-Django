from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticate_user(view_func):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        else:
            return view_func(request,*args,*kwargs)
    return inner

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def inner(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args,*kwargs)
            else:
                return HttpResponse('<h1>you are not allowed<h1>')
        return inner
    return decorator
