from administration.models import Role, Customer, Level, Features, Permission
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Account(AbstractUser):
    user_code = models.CharField(max_length=20, blank=True, verbose_name="user code")
    email = models.EmailField(unique=True, max_length=254, verbose_name="email address")
    phone = models.CharField(max_length=20, blank=True, verbose_name="phone")
    is_master = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="account_role")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="account_level")
    customer_id = models.IntegerField(default=0, verbose_name="customer id")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="date joined")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username


class FeaturesPermission(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="feature_accounts")
    feature = models.ForeignKey(Features, on_delete=models.CASCADE, related_name="per_features")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name="feature_permission")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    class Meta:
        """
        account has features and features has permission like read,edit,delete,create
        account one to one feature mapping
        """
        unique_together = ('feature', 'account')

    def __str__(self):
        return '( %s ) %s - %s' % (self.account, self.feature, self.permission)


class AccountReset(models.Model):
    username = models.CharField(max_length=150, blank=True, verbose_name="username")
    email = models.EmailField(max_length=254, verbose_name="email address")
    phone = models.CharField(max_length=20, blank=True, verbose_name="phone")
    password = models.CharField(max_length=128, verbose_name='password')
    token = models.CharField(max_length=150, verbose_name='token')
    is_used = models.BooleanField(default=False)
    token_expiry = models.DateTimeField(verbose_name="token expiry")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return self.username