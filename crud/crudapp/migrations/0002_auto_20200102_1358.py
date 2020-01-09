# Generated by Django 3.0.1 on 2020-01-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicereg',
            name='contact',
            field=models.CharField(default='', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='devicereg',
            name='email',
            field=models.EmailField(default='', editable=False, max_length=254),
        ),
        migrations.AddField(
            model_name='devicereg',
            name='username',
            field=models.CharField(default='', editable=False, max_length=30),
        ),
    ]
