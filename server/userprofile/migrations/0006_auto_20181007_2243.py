# Generated by Django 2.0.8 on 2018-10-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20181007_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.ForeignKey(on_delete='CASCADE', to='userprofile.UserCategory', verbose_name='Категория'),
        ),
    ]
