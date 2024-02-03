from django.contrib import admin
from .models import User
from .models import Admin
from .models import Cat
from .models import Photo
from .models import MedicalRecord

admin.site.register(User)
admin.site.register(Cat)
admin.site.register(Admin)
admin.site.register(Photo)
admin.site.register(MedicalRecord)

# Register your models here.
