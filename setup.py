"""
Flask-Passlib
----------

Please refer to the online documentation for details.

Links
`````

* `documentation <https://github.com/allanlei/flask-passlib>`_
"""
from setuptools import setup


setup(
    name='Flask-Passlib',
    version='0.1',
    url='https://github.com/allanlei/flask-passlib',
    license='BSD',
    author='Allan Lei',
    author_email='allanlei@helveticode.com',
    description='Flask extension for passlib',
    long_description=__doc__,
    py_modules=[
        'flask_passlib',
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'passlib==1.6.1',
        'Werkzeug>=0.6.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)