from django.db import models


# Create your models here.
class SampleStoreList(models.Model):
    seq = models.CharField(primary_key=True, max_length=20, blank=True, null=False)
    regdate = models.CharField(db_column='regDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    simplenm = models.CharField(db_column='simpleNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcd = models.CharField(db_column='zipCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    telno = models.CharField(db_column='telNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    biztype = models.CharField(db_column='bizType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    biztypenm = models.CharField(db_column='bizTypeNm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    biztypedetail = models.CharField(db_column='bizTypeDetail', max_length=10, blank=True, null=True)  # Field name made lowercase.
    salescd = models.CharField(db_column='salesCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_store_list'