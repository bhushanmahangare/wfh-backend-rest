from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from import_export.admin import ImportExportModelAdmin

from administration.models import (
    Customer, 
    Level, 
    Role, 
    Permission, 
    Section, 
    Features, 
    SectionFeature, 
    RoleFeature, 
    City, 
    State, 
    Country
)

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    pass

@admin.register(Permission)
class PermissionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Features)
class FeaturesAdmin(ImportExportModelAdmin):
    pass

@admin.register(SectionFeature)
class SectionFeatureAdmin(ImportExportModelAdmin):
    pass

@admin.register(RoleFeature)
class RoleFeatureAdmin(ImportExportModelAdmin):
    pass

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    pass

@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    pass

class LevelAdmin(TreeAdmin):
    form = movenodeform_factory(Level)
    
admin.site.register(Level, LevelAdmin)