from django.db import models
from django.utils import timezone

from treebeard.mp_tree import MP_Node

from helper.enums import CustomerStatus, DateFormat, LevelType


class Role(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return self.name


class Features(models.Model):
    display_name = models.CharField(max_length=150)
    key = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return self.key


class SectionFeature(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="Section_features")
    feature = models.ForeignKey(Features, on_delete=models.CASCADE, related_name="Section_features")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return '%s - %s' % (self.section, self.feature)


class RoleFeature(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="Roles")
    feature = models.ForeignKey(Features, on_delete=models.CASCADE, related_name="Role_features")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="date created")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    class Meta:
        """
        account has features and features has permission like read,edit,delete,create
        account one to one feature mapping
        """
        unique_together = ('role', 'feature')

    def __str__(self):
        return '%s - %s' % (self.role, self.feature)


class Level(MP_Node):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=20, choices=LevelType.choices(), default=LevelType.GROUP)
    country = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)

    node_order_by = ['name']

    def get_level_type_label(self):
        return LevelType(self.type).name.title()

    def __str__(self):
        return '%s - %s - %s' % (self.id, self.name, self.type)

    def __unicode__(self):
        return 'Level: %s' % self.name


class Customer(models.Model):
    customer_code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254, verbose_name="email address")
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=150)
    currency = models.CharField(max_length=20)
    realm = models.CharField(unique=True, max_length=20)
    logo_url = models.URLField(max_length=200, blank=True)
    home_page_url = models.URLField(max_length=200, blank=True)
    google_map_key = models.CharField(max_length=254, blank=True)
    timezone_name = models.CharField(max_length=150)
    date_format = models.PositiveIntegerField(choices=DateFormat.choices(), default=DateFormat.d_m_Y)
    level = models.OneToOneField(Level, on_delete=models.CASCADE, related_name="customer_level")
    status = models.CharField(max_length=20, choices=CustomerStatus.choices(), default=CustomerStatus.ACTIVE)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="date joined")
    date_modified = models.DateTimeField(default=timezone.now, verbose_name="date modified")

    def __str__(self):
        return self.name

    def get_customer_status_label(self):
        return CustomerStatus(self.status).name.title()
    

class Country(models.Model):
    name = models.CharField(max_length=150, blank=False)
    short_name = models.CharField(max_length=5, blank=False)
    phone_code = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return '(%d) %s' % (self.id, self.name)


class State(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,  related_name="state_country_code")

    def __str__(self):
        return '(%d)%s / %s' % (self.id, self.name, self.country)


class City(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE,  related_name="city_state_code")

    def __str__(self):
        return '(%d)%s / %s' % (self.id, self.name, self.state)