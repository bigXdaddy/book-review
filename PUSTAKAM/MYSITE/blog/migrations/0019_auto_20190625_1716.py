# Generated by Django 2.2.2 on 2019-06-25 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Book'),
        ),
    ]
