# Generated by Django 4.2.1 on 2023-07-28 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_task_options_alter_task_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task_name',
            options={'ordering': ['name'], 'verbose_name': 'TaskName', 'verbose_name_plural': 'TaskNames'},
        ),
    ]
