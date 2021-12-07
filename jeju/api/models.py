from django.db import models


# Create your models here.
class SampleCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    seq = models.ForeignKey('SampleStoreList', models.DO_NOTHING, db_column='seq')
    category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sample_category'


class SampleStoreList(models.Model):
    seq = models.CharField(primary_key=True, max_length=20)
    simplenm = models.CharField(db_column='simpleNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_store_list'