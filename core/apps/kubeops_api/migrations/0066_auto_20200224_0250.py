# Generated by Django 2.2.10 on 2020-02-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0065_itemrole'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='users',
            new_name='profiles',
        ),
        migrations.AlterField(
            model_name='clusterhealthhistory',
            name='date_type',
            field=models.CharField(choices=[('HOUR', 'HOUR'), ('DAY', 'DAY')], default='HOUR', max_length=255),
        ),
        migrations.AlterField(
            model_name='itemrole',
            name='role',
            field=models.CharField(choices=[('VIEWER', 'viewer'), ('MANAGER', 'manager')], max_length=128, unique=True),
        ),
    ]