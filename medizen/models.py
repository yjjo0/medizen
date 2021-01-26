from django.db import models

 # Examination table model
class Examination(models.Model):
    ex_sn = models.IntegerField(primary_key=True)
    ex_clt_nm = models.CharField(max_length=100, blank=True, null=True)
    ex_cd = models.CharField(max_length=100, blank=True, null=True)
    ex_obj_nm = models.CharField(max_length=100, blank=True, null=True)
    ex_sex = models.CharField(max_length=100, blank=True, null=True)
    ex_date = models.DateField(blank=True, null=True)
    ex_pkg_nm = models.CharField(max_length=100, blank=True, null=True)
    ex_pkg_cd = models.CharField(max_length=100, blank=True, null=True)
    ex_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examination'

 # Disease table model
class Disease(models.Model):
    ds_cd = models.CharField(primary_key=True, max_length=100)
    ds_nm_kr = models.CharField(max_length=100, blank=True, null=True)
    ds_nm_en = models.CharField(max_length=100, blank=True, null=True)
    ds_def = models.CharField(max_length=3400, blank=True, null=True)
    ds_cau = models.CharField(max_length=3400, blank=True, null=True)
    ds_sym = models.CharField(max_length=3400, blank=True, null=True)
    ds_dx = models.CharField(max_length=3400, blank=True, null=True)
    ds_tx = models.CharField(max_length=3400, blank=True, null=True)
    ds_prev = models.CharField(max_length=3400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'
        
 # Diagnosis table model
class Diagnosis(models.Model):
    ex_sn = models.OneToOneField('Examination', models.DO_NOTHING, db_column='ex_sn', primary_key=True)
    ds_cd = models.ForeignKey('Disease', models.DO_NOTHING, db_column='ds_cd')
    dx_po = models.FloatField(blank=True, null=True)
    dx_rr = models.FloatField(blank=True, null=True)
    dx_deg = models.CharField(max_length=100, blank=True, null=True)
    dx_smry = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'
        unique_together = (('ex_sn', 'ds_cd'),) # composite key : ex_sn & ds_cd