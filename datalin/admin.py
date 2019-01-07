from django.contrib import admin

from .models import Technology, Entity, Node, Application, Relation_Type

# Register your models here.

admin.site.register(Technology)
admin.site.register(Entity)
admin.site.register(Node)
admin.site.register(Application)
admin.site.register(Relation_Type)