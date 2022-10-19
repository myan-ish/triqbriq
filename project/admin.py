from django.contrib import admin

from project.models import Project, Customer, Address, Birq

admin.site.register(Project)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Birq)