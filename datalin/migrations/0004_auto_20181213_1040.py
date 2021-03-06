# Generated by Django 2.1.2 on 2018-12-13 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datalin', '0003_auto_20181118_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='relation_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='entity',
            name='technology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datalin.Technology'),
        ),
    ]
