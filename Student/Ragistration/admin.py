from django.contrib import admin
from.models import Apply
from.models import Signup1
from.models import Post
from.models import Contact

# Register your models here.
class ApplyAdmin(admin.ModelAdmin):
    list_display=['Job_Role','Qualification','Experience','Location','Offical_Websitee']

    list_filter = ('Job_Role','Qualification','Experience','Location')

    search_fields = ('Job_Role','Qualification','Experience','Location')

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','college','subject','feedback']

    list_filter = ('name','email','college')

    search_fields = ('name','email','college')


admin.site.register(Apply,ApplyAdmin)
admin.site.register(Signup1)
admin.site.register(Post)
admin.site.register(Contact,ContactAdmin)