# Generated by Django 5.0.6 on 2024-05-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='pic',
            field=models.FileField(upload_to='<bound method Field.value_from_object of <django.db.models.fields.CharField>>'),
        ),
    ]
