# Generated by Django 2.2.2 on 2019-06-23 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190623_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='writerofthebook',
            new_name='writer',
        ),
    ]
