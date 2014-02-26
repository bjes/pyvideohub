from pyramid.view import view_config
from . import forms
from deform import Form


@view_config(route_name='home', renderer='pyvideohub:templates/home.jinja2')
def home_view(request):
    return {}

@view_config(route_name='upload', renderer='pyvideohub:templates/upload.jinja2')
def upload_view(request):
    form = Form(forms.UploadSchema())
    return {'form': form}

@view_config(route_name='about', renderer='pyvideohub:templates/about.jinja2')
def about_view(request):
    return {}

@view_config(route_name='contact_us', renderer='pyvideohub:templates/contact_us.jinja2')
def contact_us_view(request):
    return {}
