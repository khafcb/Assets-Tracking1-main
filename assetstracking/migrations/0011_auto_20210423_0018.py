# Generated by Django 3.1.7 on 2021-04-22 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetstracking', '0010_auto_20210422_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='subscriber_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='subscriber_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
        migrations.AlterField(
            model_name='rfid',
            name='subscriber_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='subscriber_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assetstracking.subscriber'),
        ),
    ]
