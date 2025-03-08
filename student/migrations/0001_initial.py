# Generated by Django 5.1.7 on 2025-03-08 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='common',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.common')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('branch', models.CharField(blank=True, max_length=30, null=True)),
            ],
            bases=('student.common',),
        ),
    ]
