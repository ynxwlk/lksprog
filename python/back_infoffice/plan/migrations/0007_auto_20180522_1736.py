# Generated by Django 2.0.3 on 2018-05-22 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_auto_20180522_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xiangmu',
            old_name='BianHao',
            new_name='xmBianHao',
        ),
        migrations.RenameField(
            model_name='xiangmu',
            old_name='FaGaiPiWen',
            new_name='xmFaGaiPiWen',
        ),
        migrations.RenameField(
            model_name='xiangmu',
            old_name='JianSheDanWei',
            new_name='xmJianSheDanWei',
        ),
        migrations.RenameField(
            model_name='xiangmu',
            old_name='JianShedidian',
            new_name='xmJianShedidian',
        ),
        migrations.RenameField(
            model_name='xiangmu',
            old_name='MinCheng',
            new_name='xmMinCheng',
        ),
        migrations.RenameField(
            model_name='xiangmu',
            old_name='creation',
            new_name='xmcreation',
        ),
    ]