# Generated by Django 3.0.1 on 2020-01-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_auto_20200102_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicereg',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='devicereg',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='devicereg',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
