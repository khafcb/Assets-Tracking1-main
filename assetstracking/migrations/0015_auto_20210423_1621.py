# Generated by Django 3.1.7 on 2021-04-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetstracking', '0014_auto_20210423_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowing',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='rfid',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='borrowing',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assetstracking.subscriber'),
        ),
        migrations.AddField(
            model_name='employee',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assetstracking.subscriber'),
        ),
        migrations.AddField(
            model_name='rfid',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assetstracking.subscriber'),
        ),
        migrations.AddField(
            model_name='tag',
            name='subscriber_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assetstracking.subscriber'),
        ),
    ]
