import urllib
import csv
import json
import pandas as pd
import sys
import subprocess
import random
from SimpleCV import Image

#assign the number of photos, and root API call to variables
number_photos = int(sys.argv[1])
api_call_root = sys.argv[2]
pages = number_photos / 100

#this number can be changed in order to denote the specific script run time, this variable is used in naming the JSON and CSV files
datafile_count = 1

# this code hits the PIXLEE API, and saves the JSON response to file
fh = open('data_files/jsondata' + str(datafile_count) + '.json', 'w')
for count in range(0, pages):
    url = api_call_root + str(count)
    response = urllib.urlopen(url)

    status = response.getcode()
    if status == 200:
        body = response.read()
        fh.write(body+'\n')
        print "Successfully requested %s" % url
    else:
        print "Failed to request %s " % url

#these functions deal with all of the difficulites with encoding / decoding the data into the proper format
def utf_encode(data):
    if isinstance(data, basestring):
        return data.encode('utf8')
    return data

def utf_encode_dict(data):
        return dict(map(utf_encode, pair) for pair in data.items())

#open the csv to be written, and write the headers
#code deleted to protect the privacy of PIXLEE

#write the json objects to csv
#code deleted to protect the privacy of PIXLEE


#Download the photos to the server
api_csv = pd.read_csv("data_files/csvdata" + str(datafile_count) + ".csv")
photo_count = -1;
for url in api_csv["photo_url"]:
    photo_count += 1
    if photo_count < number_photos:
      if isinstance(url, str):
        if "http://" in url:
            if ".jpg" in url:
                print url
                print photo_count
                urllib.urlretrieve(url, "photos/" + str(datafile_count) + str(photo_count) + ".jpg")
first_photo_name = "can"

#generate a random id for the template and save it to file
randomString1 = str(random.random()) + str(random.random()) + str(random.random()) + str(random.random())
randomString2 = str(random.random()) + str(random.random()) + str(random.random()) + str(random.random())
canTemplate = subprocess.call("s3cmd get " + sys.argv[3] + " " + "templates/" + randomString1 + ".jpg", shell=True)
logoTemplate = subprocess.call("s3cmd get " + sys.argv[4] + " " + "templates/" + randomString2 + ".jpg", shell=True)
can = Image("templates/" + randomString1 + ".jpg")
logo = Image("templates/" + randomString2 + ".jpg")

#initialize the csv file that just contains the filtering data
columns = ['can', 'logo', 'bottle']
index = range(0, number_photos)
df = pd.DataFrame(index=index, columns=columns)

#add additional columns to the previously created csv file to account for the filtered data information
old_csv = pd.read_csv("data_files/csvdata" + str(datafile_count) + ".csv")
old_csv["can"] = ''
old_csv["logo"] = ''

#loop through all of the photos, evaluate the against the template
#if the photo contains the templates, update the csv files, and save the photo to an s3 bucket
analyze_count = 0
while analyze_count < photo_count:
  location = "photos/" + str(datafile_count) + str(analyze_count) + ".jpg"
  print location
  try:
    img = Image(location)
    print img
    if img:
      canmatch = img.findKeypointMatch(can)
      if canmatch:
        df.ix[analyze_count,0] = 1
        old_csv.ix[analyze_count,"can"] = 1
        subprocess.call("s3cmd put photos/" + str(datafile_count) + str(analyze_count) + ".jpg s3://can_photos/" + str(datafile_count) + str(analyze_count) + ".jpg", shell=True)
        img.save("can_photos/" + str(datafile_count) + str(analyze_count) + ".jpg")
      logomatch = img.findKeypointMatch(logo)
      if logomatch:
        df.ix[analyze_count,1] = 1
        old_csv.ix[analyze_count,"logo"] = 1
        subprocess.call("s3cmd put photos/" + str(datafile_count) + str(analyze_count) + ".jpg s3://logo_photos/" + str(datafile_count) + str(analyze_count) + ".jpg", shell=True)
        img.save("logo_photos/" + str(datafile_count) + str(analyze_count) + ".jpg")
  except:
    pass
  analyze_count+=1

df.to_csv("data_files/scored_coke_product_face.csv")
old_csv.to_csv("data_files/scored_with_complete_data.csv")

datafile_count += 1