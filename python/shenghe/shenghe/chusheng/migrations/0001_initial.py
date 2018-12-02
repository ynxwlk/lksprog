# Generated by Django 2.0.1 on 2018-02-12 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JianSheDanWei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jianshedanwei_name', models.CharField(default='abc', max_length=128)),
                ('jianshedanwei_dizhi', models.CharField(max_length=128)),
                ('jianshedanwei_fadingdaibiaoren', models.CharField(max_length=8)),
                ('jianshedanwei_fadingdaibiaorendianhua', models.CharField(max_length=11)),
                ('jianshedanwei_lianxiren', models.CharField(max_length=8)),
                ('jianshedanwei_lianxirendianhua', models.CharField(max_length=11)),
                ('jianshedanwei_dianhua', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='XiangMu',
            fields=[
                ('bianhao', models.AutoField(primary_key=True, serialize=False)),
                ('mincheng', models.CharField(max_length=128)),
                ('jianshedidian', models.CharField(max_length=128)),
                ('jianshedanwei', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chusheng.JianSheDanWei')),
            ],
        ),
    ]