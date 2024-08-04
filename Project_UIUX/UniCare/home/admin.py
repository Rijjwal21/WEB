from django.contrib import admin
from home.models import Doctor
from home.models import Patient
from home.models import Uniqueid
from home.models import Document
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Uniqueid)
admin.site.register(Document)