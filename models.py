# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Whitelistrecdata(models.Model):
    wid = models.AutoField(db_column='WID', primary_key=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='MemberID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wlid = models.IntegerField(db_column='WLID')  # Field name made lowercase.
    addeddate = models.TextField(db_column='AddedDate', blank=True, null=True)  # Field name made lowercase.
    addedby = models.IntegerField(db_column='AddedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhiteListRecData'
