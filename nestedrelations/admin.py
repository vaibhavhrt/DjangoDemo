from django.contrib import admin

from nestedrelations.models import Parent, ChildA, ChildB, ChildA1, ChildA2

# Register your models here.
# class ParentAdmin(admin.ModelAdmin):
#     model = Parent

admin.site.register(Parent)
admin.site.register(ChildA)
admin.site.register(ChildB)
admin.site.register(ChildA1)
admin.site.register(ChildA2)
