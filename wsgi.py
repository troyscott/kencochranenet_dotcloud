import os
import sys

# Ken added this, only thing that is different from the example template (not counting settings file name)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'mysite')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django.core.handlers.wsgi
djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)