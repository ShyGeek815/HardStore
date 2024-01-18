from django.contrib import admin
 # импортирую модели, которые я создала отдельно 
from .models import Record
from .models import HardStore_record
from .models import Storehouse
from .models import Employee
 
# регистрация в разделе администрация сайта (admin)
admin.site.register(Record)

# регистрация в разделе администрация сайта (admin)
admin.site.register(Employee)

# регистрация в разделе администрация сайта (admin)
admin.site.register(HardStore_record)

# регистрация в разделе администрация сайта (admin)
admin.site.register(Storehouse)