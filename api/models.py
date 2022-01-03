from django.db import models


class Stay(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    numofrooms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stay'
