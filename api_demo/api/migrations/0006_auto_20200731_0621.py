# Generated by Django 2.2.1 on 2020-07-31 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_attachments_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='last_modified_by',
        ),
        migrations.DeleteModel(
            name='MetaData',
        ),
        migrations.AlterModelOptions(
            name='attachments',
            options={'verbose_name_plural': 'Attachments'},
        ),
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name_plural': 'Notes'},
        ),
        migrations.DeleteModel(
            name='Logs',
        ),
    ]
