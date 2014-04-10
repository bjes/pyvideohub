from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from . import forms
from .models import DBSession

@view_config(route_name='home', renderer='pyvideohub:templates/home.jinja2')
def home_view(request):
    return {}

@view_config(route_name='upload', renderer='pyvideohub:templates/upload.jinja2',
             request_method='GET')
def upload_view_via_get(request):
    form = forms.UploadForm()
    return {'form': form}

@view_config(route_name='upload', renderer='pyvideohub:templates/upload.jinja2',
             request_method='POST')
def upload_view_via_post(request):
    import os, datetime
    from .models import Video
    form = forms.UploadForm(request.POST)
    if form.validate():
        with DBSession() as db:
            new_video = Video()
            form.populate_obj(new_video)
            db.add(new_video)
            db.commit()

            # 將檔案寫入 video.store_path 路徑
            today = datetime.datetime.today()
            store_path = request.registry.settings['video.store_path']
            new_file_name = ''.join(['tmp-', str(new_video.id),
                                    os.path.splitext(request.POST[form.file.name].filename)[1]])
            dst_path_basedir = os.path.join(store_path, str(today.year), str(today.month))
            dst_path = os.path.join(dst_path_basedir, new_file_name)
            if not os.path.exists(dst_path_basedir):
                try:
                    os.makedirs(dst_path_basedir)
                except OSError:
                    # Race condition handling. os.mkdirs will raise OSError while the dir has already
                    # existed.
                    pass
            output_file = open(dst_path, 'wb')
            input_file = request.POST[form.file.name].file
            input_file.seek(0)
            while True:
                content = input_file.read(5120000)
                if not content:
                    break
                output_file.write(content)
            output_file.close()

            request.session.flash('新增影片成功')
            return HTTPFound('/')
    else:
        return {'form': form}

@view_config(route_name='about', renderer='pyvideohub:templates/about.jinja2')
def about_view(request):
    return {}

@view_config(route_name='contact_us', renderer='pyvideohub:templates/contact_us.jinja2')
def contact_us_view(request):
    return {}
