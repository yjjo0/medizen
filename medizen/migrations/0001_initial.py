# Generated by Django 3.1.5 on 2021-01-07 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('ds_cd', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ds_nm_kr', models.CharField(blank=True, max_length=100, null=True)),
                ('ds_nm_en', models.CharField(blank=True, max_length=100, null=True)),
                ('ds_def', models.CharField(blank=True, max_length=3400, null=True)),
                ('ds_cau', models.CharField(blank=True, max_length=3400, null=True)),
                ('ds_sym', models.CharField(blank=True, max_length=3400, null=True)),
                ('ds_dx', models.CharField(blank=True, max_length=3400, null=True)),
                ('ds_tx', models.CharField(blank=True, max_length=3400, null=True)),
                ('ds_prev', models.CharField(blank=True, max_length=3400, null=True)),
            ],
            options={
                'db_table': 'disease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('ex_sn', models.IntegerField(primary_key=True, serialize=False)),
                ('ex_clt_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('ex_cd', models.CharField(blank=True, max_length=100, null=True)),
                ('ex_obj_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('ex_sex', models.CharField(blank=True, max_length=100, null=True)),
                ('ex_date', models.DateField(blank=True, null=True)),
                ('ex_pkg_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('ex_pkg_cd', models.CharField(blank=True, max_length=100, null=True)),
                ('ex_rate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'examination',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('ex_sn', models.OneToOneField(db_column='ex_sn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='medizen.examination')),
                ('dx_po', models.FloatField(blank=True, null=True)),
                ('dx_rr', models.FloatField(blank=True, null=True)),
                ('dx_deg', models.CharField(blank=True, max_length=100, null=True)),
                ('dx_smry', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'diagnosis',
                'managed': False,
            },
        ),
    ]
