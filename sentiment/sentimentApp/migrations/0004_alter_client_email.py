# Generated by Django 3.2.4 on 2021-07-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentApp', '0003_auto_20210703_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
