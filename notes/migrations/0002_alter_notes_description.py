# Generated by Django 4.1.2 on 2023-02-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
