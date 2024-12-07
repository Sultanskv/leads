# Generated by Django 5.1.1 on 2024-10-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_super_admin_super_admin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferred_medium',
            field=models.CharField(choices=[('sms', 'SMS'), ('facebook', 'Facebook'), ('phone_call', 'Phone call')], default='facebook', help_text="Lead's preferred social media for communication", max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='source',
            field=models.CharField(blank=True, choices=[('organic_search', 'Organic Search'), ('google_ad', 'Google Ad'), ('youtube', 'YouTube'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('twitter', 'Twitter')], default='facebook', help_text='Where Lead found us', max_length=50),
        ),
        migrations.AlterField(
            model_name='super_admin',
            name='super_admin_id',
            field=models.CharField(blank=True, default='c4b446ab', max_length=8, unique=True),
        ),
    ]
