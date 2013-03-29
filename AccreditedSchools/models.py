from django.db import models

class AccreditedSchool(models.Model):
  Institution_ID           = models.IntegerField()
  Institution_Name         = models.CharField(max_length=200)
  Institution_Address      = models.CharField(max_length=200)
  Institution_City         = models.CharField(max_length = 30)
  Institution_State        = models.CharField(max_length = 30)
  Institution_Zip          = models.CharField(max_length = 20)
  Institution_Phone        = models.CharField(max_length = 20)
  Institution_OPEID        = models.CharField(max_length = 10)
  Institution_IPEDS_UnitID = models.CharField(max_length = 10, null=True, blank=True)

  Institution_Web_Address  = models.URLField(max_length = 100)
  Campus_ID                = models.CharField(max_length = 5, null=True, blank=True)
  Campus_Name              = models.CharField(max_length = 100)
  Campus_Address           = models.CharField(max_length = 200)
  Campus_City              = models.CharField(max_length = 30)
  Campus_State             = models.CharField(max_length = 30)
  Campus_Zip               = models.CharField(max_length = 20)
  Campus_IPEDS_UnitID      = models.CharField(max_length = 10,null=True, blank=True)
  Accreditation_Type       = models.CharField(max_length = 20)
  Agency_Name              = models.CharField(max_length = 200)
  Agency_Status            = models.CharField(max_length = 50)
  Program_Name             = models.CharField(max_length = 200)
  Accreditation_Status     = models.CharField(max_length = 20)
  Accreditation_Date_Type  = models.CharField(max_length = 20)
  Periods                  = models.CharField(max_length = 30)
  Last_Action              = models.CharField(max_length = 30)


  def __unicode__(self):
    return "%d, %s" % (self.Institution_ID, self.Institution_Name)
