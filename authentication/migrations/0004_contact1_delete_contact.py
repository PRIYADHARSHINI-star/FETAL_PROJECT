# Generated by Django 4.1.5 on 2023-02-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('Messages', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]