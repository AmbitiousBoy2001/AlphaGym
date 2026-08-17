from django.contrib import admin
from authapp.models import Contact, Enrollment, MembershipPlan, Trainer, Gallery, Attendance

admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)

# Register your models here.
