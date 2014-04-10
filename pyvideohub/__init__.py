from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config
from .models import ScopedSession, Base


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = SignedCookieSessionFactory(settings['session.secret'])

    engine = engine_from_config(settings, 'sqlalchemy.')
    ScopedSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings, session_factory=session_factory)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'pyvideohub:static', cache_max_age=3600)
    config.add_static_view('videos', 'pyvideohub:videos', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('upload', '/upload')
    config.add_route('about', '/about')
    config.add_route('contact_us', '/contact_us')
    config.scan()
    return config.make_wsgi_app()
