# Generated by Django 2.2 on 2019-06-20 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('market', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secu_infos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]