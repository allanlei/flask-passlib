from .context import flask_context
from passlib.context import LazyCryptContext


class Passlib(object):
    def __init__(self, app=None, **kwargs):
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, context=flask_context, schemes=None):
        self.app = app
        
        # register extension with app
        self.app.extensions = getattr(app, 'extensions', {})
        self.app.extensions['passlib'] = self

        self.context = context

    def verify(self, *args, **kwargs):
        return self.context.verify(*args, **kwargs)

    def encrypt(self, *args, **kwargs):
        if 'salt_length' in kwargs:
            kwargs['salt_size'] = kwargs.pop('salt_length')
        if 'method' in kwargs:
            kwargs['scheme'] = kwargs.pop('method')
        return self.context.encrypt(*args, **kwargs)

    def identify(self, *args, **kwargs):
        return self.context.identify(*args, **kwargs)