# Generated by Django 2.0.5 on 2018-05-04 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_exam', models.CharField(max_length=100)),
                ('second_exam', models.CharField(max_length=100)),
                ('third_exam', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
