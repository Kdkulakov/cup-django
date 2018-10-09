# Generated by Django 2.0.8 on 2018-10-07 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20181007_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercategory',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='usercompany',
            options={'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='usercategory',
            name='description',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserCategory'),
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]