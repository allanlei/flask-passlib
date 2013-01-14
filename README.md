## Flask-Passlib ##

Flask extension for [Passlib](http://packages.python.org/passlib/).

This is still WIP, but give it a try.

### Installation ###

```pip install Flask-Passlib```

### Usage ###

The default usage will attempt to figure out what version of ```werkzeug``` is being used. 
As of ```werkzeug <= 0.8.3``` only supports MD5 and SHA1. 
```python
app = Flask(__name__)
passlib = Passlib(app)
```

To change the ```passlib``` schemes, initialize with an instance of CryptContext and set the ```default``` scheme.

```python
from passlib.context import LaxyCryptContext
from flask.ext.passlib.context import (werkzeug_salted_md5, werkzeug_salted_sha1, 
    werkzeug_salted_sha256, werkzeug_salted_sha512)
from passlib.hash import django_pbkdf2_sha256

passlib = Passlib(app, context=LazyCryptContext(
    schemes=[
        werkzeug_salted_md5,
        werkzeug_salted_sha1,
        werkzeug_salted_sha256,
        werkzeug_salted_sha512,         

        django_pbkdf2_sha256,
    ],
    default='django_pbkdf2_sha256',
))
```

In this example, we have the Flask defaults with __Django's PBKDF2 SHA256__.

##### Verifying #####

In Flask using werkzeug's

```python
check_password_hash(password_hash, raw_password)
```

With Flask-Passlib

```python
passlib.verify(raw_password, password_hash)
```

##### Generating #####

In Flask using werkzeug's

```python
generate_password_hash(raw_password, method=.., salt_length=..)
```

With Flask-Passlib

```python
passlib.encrypt(raw_password, method=..., salt_length=...)
```
### Documentation ###
Also check out [Passlib's documentation](http://packages.python.org/passlib/)
