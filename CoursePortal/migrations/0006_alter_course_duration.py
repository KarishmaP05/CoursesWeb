# Generated by Django 4.1.1 on 2024-02-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursePortal', '0005_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.TimeField(),
        ),
    ]