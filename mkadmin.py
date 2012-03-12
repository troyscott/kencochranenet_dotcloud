#!/usr/bin/env python
from wsgi import *
from django.contrib.auth.models import User
u, created = User.objects.get_or_create(username='admin')
if created:
    u.set_password('P@s$w0rd1')
    u.is_superuser = True
    u.is_staff = True
    u.save()

# once done, login immediately and change the password to something more secure.