from django.contrib import admin
from hositalapp.models import *


# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(staff)
admin.site.register(ward)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Transaction)


