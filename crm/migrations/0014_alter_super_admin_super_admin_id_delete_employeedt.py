# Generated by Django 5.1.1 on 2024-12-01 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_alter_super_admin_super_admin_id_employeedt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super_admin',
            name='super_admin_id',
            field=models.CharField(blank=True, default='779531f1', max_length=8, unique=True),
        ),
        migrations.DeleteModel(
            name='EmployeeDT',
        ),
    ]