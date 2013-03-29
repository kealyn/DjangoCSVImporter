# ==============================================================================
# CSV Importer
#
# Description: A python program that allows developers to import CSV files and
#              map their data to models, mapping column headers to model fields
#              in the data migration section downwards.
#
# Author     : Lin Qi
# Created on : Mar. 25th, 2013
# Updated on : Mar. 25th, 2013
# ==============================================================================

import sys,os
import csv
from django.conf import settings
from AccreditedSchools import AccreditedSchools_defaults


settings.configure(default_settings = AccreditedSchools_defaults, DEBUG = True)


PROJECT_ROOT = os.path.realpath('..') 
print PROJECT_ROOT
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'AccreditedSchools'))

# ========
# Settings
# ========
# Full path and name to the csv file
#csv_filepathname="./Accreditation_2012_12.csv"
csv_filepathname= os.path.realpath('') + "/test.csv"

# Full path to the django project directory
your_djangoproject_home=os.path.realpath('..')

# Database setting file path
settings_path = "csvImporter.settings"

# Setting path
sys.path.append(your_djangoproject_home)
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)


# Import django model
# Format: from YOURAPP.models import YOURMODEL
from AccreditedSchools.models import AccreditedSchool

# set your csv data delimiter
data_delimiter = '|'

# ====
# Data migration section: Mapping column headers to model fields
# ====
from time import clock, time
counter = 0;
start = time()
with open(csv_filepathname, 'rb') as csvfile:
  spamreader = csv.reader( csvfile, delimiter = data_delimiter) 
  for row in spamreader:
    # Make modifications here
    ####
    # Constructor
    schoolModel = AccreditedSchool()
    # Load data
    schoolModel.Institution_ID           = row[0]
    schoolModel.Institution_Name         = row[1]
    schoolModel.Institution_Address      = row[2]
    schoolModel.Institution_City         = row[3]
    schoolModel.Institution_State        = row[4]
    schoolModel.Institution_Zip          = row[5]
    schoolModel.Institution_Phone        = row[6]
    schoolModel.Institution_OPEID        = row[7]
    schoolModel.Institution_IPEDS_UnitID = row[8]
    schoolModel.Institution_Web_Address  = row[9]
    schoolModel.Campus_ID                = row[10]
    schoolModel.Campus_Name              = row[11]
    schoolModel.Campus_Address           = row[12]
    schoolModel.Campus_City              = row[13]
    schoolModel.Campus_State             = row[14]
    schoolModel.Campus_Zip               = row[15]
    schoolModel.Campus_IPEDS_UnitID      = row[16]
    schoolModel.Accreditation_Type       = row[17]
    schoolModel.Agency_Name              = row[18]
    schoolModel.Agency_Status            = row[19]
    schoolModel.Program_Name             = row[20]
    schoolModel.Accreditation_Status     = row[21]
    schoolModel.Accreditation_Date_Type  = row[22]
    schoolModel.Periods                  = row[23]
    schoolModel.Last_Action              = row[24]
    schoolModel.save()
    # counter update
    counter = counter + 1
    ####
    # End modifications

elapsed = (time() - start)
print ("Loading from csv file " + csv_filepathname + "...")
print (str(counter) + " lines have been migrated into the database.")
print ("Loading finished, total time consuming: " + str(elapsed) + " seconds.")
