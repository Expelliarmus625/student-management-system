# Generated by Django 2.2.5 on 2019-09-12 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190912_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Subjects'),
        ),
    ]
