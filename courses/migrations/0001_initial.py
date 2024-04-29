# Generated by Django 5.0.4 on 2024-04-28 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructor_name', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('prerequisites', models.ManyToManyField(blank=True, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
