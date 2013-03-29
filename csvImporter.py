# =============================================================================
# CSV Importer
#
# Description: A python program that allows developers to import CSV files and
#              map their data to models, mapping column headers to model fields
#              in the data migration section downwards.
#
# Usage:
#   To run this script, go to the project root folder, and do the following:
#     1. In cmd line prompt, type 'python manage.py shell' to enter the python
#        shell
#     2. In python shell, type 'import schools.csvImporter'
#     3. Then, just type 'schools.csvImporter.run()' to run this script
#
# Author     : Lin Qi
# Created on : Mar. 25th, 2013
# Updated on : Mar. 28th, 2013
# =============================================================================



def run():
  import sys,os
  import csv
  import urllib
  import zipfile
  import shutil

  # settings for the zip file
  # Change these names if new release comes out
  # -------
  data_csv_file_zip_name = "Accreditation_2012_12.zip"
  data_csv_file_name = "Accreditation_2012_12.csv"
  data_xls_file_name = "Accreditation_2012_12.xls"
  data_readme = "ReadMe.doc"
  # -------

  # download the file
  urllib.urlretrieve ("http://ope.ed.gov/accreditation/dataFiles/" + data_csv_file_zip_name, data_csv_file_zip_name)

  # unzip process
  zfile = zipfile.ZipFile(data_csv_file_zip_name)

  for name in zfile.namelist():
    (dirname, filename) = os.path.split(name)
    if dirname == '':
      # file
      fd = open(name, 'w')
      fd.write(zfile.read(name))
      fd.close()
    else:
      # directory
      if not os.path.exists(dirname):
        os.mkdir(dirname)
      # file
      fd = open(name, 'w')
      fd.write(zfile.read(name))
      fd.close()

  zfile.close()


  # csv process

  # ========
  # Settings
  # ========
  # Full path and name to the csv file
  csv_filepathname= os.path.realpath('') + "/" + data_csv_file_name

  # Full path to the django project directory
  your_djangoproject_home=os.path.realpath('')

  # Database setting file path
  #settings_path = "csvImporter.settings"

  # Setting path
  #os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)
  #sys.path.append(your_djangoproject_home)

  # Import django model
  # Format: from YOURAPP.models import YOURMODEL
  # uncomment next line for local testing
  # from AccreditedSchools.models import AccreditedSchool
  from schools.models import AccreditedSchool

  # set your csv data delimiter
  data_delimiter = ','

  # ====
  # Data migration section: Mapping column headers to model fields
  # ====
  from time import clock, time
  counter = 0;
  start = time()
  with open(csv_filepathname, 'rb') as csvfile:
    spamreader = csv.reader( csvfile, delimiter = data_delimiter)
    next(spamreaderc, None)
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

  # delete process
  for root, dirs, files in os.walk(os.path.realpath('')):
    for f in files:
      if f == data_csv_file_zip_name or f == data_xls_file_name or \
      f == data_readme:
        os.unlink(os.path.join(root, f))
