# Generated by Django 2.2.2 on 2019-06-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190622_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='writer',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='writer',
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ManyToManyField(help_text='Select a writer for this book', to='blog.Writer'),
        ),
    ]