# Generated by Django 3.1.6 on 2021-02-09 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecart', '0002_auto_20210209_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecart',
            name='category',
        ),
        migrations.AlterField(
            model_name='ecart',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecart.categorymap'),
        ),
    ]