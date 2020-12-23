# Generated by Django 3.0.8 on 2020-12-23 17:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('user_code', models.CharField(blank=True, max_length=20, verbose_name='user code')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='phone')),
                ('is_master', models.BooleanField(default=False)),
                ('customer_id', models.IntegerField(default=0, verbose_name='customer id')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date modified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_level', to='administration.Level')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_role', to='administration.Role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='phone')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('token', models.CharField(max_length=150, verbose_name='token')),
                ('is_used', models.BooleanField(default=False)),
                ('token_expiry', models.DateTimeField(verbose_name='token expiry')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date modified')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturesPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date modified')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_accounts', to=settings.AUTH_USER_MODEL)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='per_features', to='administration.Features')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_permission', to='administration.Permission')),
            ],
            options={
                'unique_together': {('feature', 'account')},
            },
        ),
    ]
