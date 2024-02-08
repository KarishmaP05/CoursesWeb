# Generated by Django 4.1.1 on 2024-02-06 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursePortal', '0009_alter_course_category_alter_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('course_preferences', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 6)),
        ),
    ]