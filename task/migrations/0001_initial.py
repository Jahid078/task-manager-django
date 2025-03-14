# Generated by Django 5.1.7 on 2025-03-08 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
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
            name='Task',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='task.common')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Cancel'), ('A', 'Approved'), ('CD', 'Completed')], default='P', max_length=10)),
                ('priority_choices', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10)),
                ('student_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_task', to='student.student')),
                ('teacher_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_task', to='teacher.teacher')),
            ],
            bases=('task.common',),
        ),
    ]
