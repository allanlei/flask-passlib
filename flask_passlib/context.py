from distutils.version import StrictVersion
from passlib.context import LazyCryptContext
import werkzeug

from .handlers import (werkzeug_salted_md5, werkzeug_salted_sha1, 
    werkzeug_salted_sha224, werkzeug_salted_sha256, 
    werkzeug_salted_sha384, werkzeug_salted_sha512)


werkzeug061_context = LazyCryptContext(
    schemes=[
        werkzeug_salted_md5,    
        werkzeug_salted_sha1,
    ],
    default='werkzeug_salted_sha1',
)

werkzeugdev_context = LazyCryptContext(
    schemes=[
        werkzeug_salted_md5,    
        werkzeug_salted_sha1,
        werkzeug_salted_sha224,
        werkzeug_salted_sha256,
        werkzeug_salted_sha384,
        werkzeug_salted_sha512,
    ],
    default='werkzeug_salted_sha1',
)


if StrictVersion('0.6.1') <= StrictVersion(werkzeug.__version__) <= StrictVersion('0.8.3'):
    werkzeug_context = werkzeug061_context
elif StrictVersion(werkzeug.__version__) > StrictVersion('0.8.3'):
    werkzeug_context = werkzeugdev_context
else:
    werkzeug_context = werkzeug061_context

flask_context = werkzeug_context