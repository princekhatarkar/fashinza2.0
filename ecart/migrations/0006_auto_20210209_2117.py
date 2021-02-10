# Generated by Django 3.1.6 on 2021-02-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecart', '0005_auto_20210209_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorymap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='ecart',
            name='category',
        ),
        migrations.AddField(
            model_name='ecart',
            name='category_id',
            field=models.ManyToManyField(to='ecart.categorymap'),
        ),
    ]
