# Generated by Django 4.1.7 on 2023-03-20 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='created_on',
        ),
    ]