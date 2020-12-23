from django.contrib import admin
from authentication.models import Account, FeaturesPermission, AccountReset

admin.site.register(Account)
admin.site.register(FeaturesPermission)
admin.site.register(AccountReset)