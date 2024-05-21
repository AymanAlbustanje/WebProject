# Generated by Django 4.2.11 on 2024-05-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_enrollment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='schedule',
        ),
        migrations.AlterField(
            model_name='course',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='enrollment_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]