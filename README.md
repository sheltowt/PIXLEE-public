PIXLEE-public
=============

PIXLEE Computer Vision System

The purpose of this project is to provide PIXLEE with a system that will take a template, and filter photos from a clients social media stream by that template. The example data used for this system is from Coke, and the templates used to filter were a picture of a can, and a picture of the coke logo. A visualization of the original and filtered images was created by Greg Palmer- https://github.com/g-palmer/, and is viewable at http://computer-vision-example-pixlee.nodejitsu.com/.

PIXLEE provides technologies that enable clients to collect, display and measure user-generated photos, as well as leverage their photos to drive traffic and increase sales. Currently photos are filtered manually, and PIXLEE has no methodology to automatically select images that contain a certain image. I developed a script that does this, and uploaded it to a ubuntu server connected to S3 buckets that allow for easy access to templates, and export of filtered photos.

Filtering Process-

Upload template to be filtered to S3
Enter command line inputs on EC2 Ubuntu server
Retrieve JSON objects from API
Convert to CSV (later used to score photos that contain the template)
Retrieve photos and store to server
Analyze photos
Output filtered photos to S3, scored data to CSV file
Command Line Inputs-

python master_FINAL.py 400 ‘http://APIROOT' 's3://HACKREACTOR/can.jpg’ ‘s3://HACKREACTOR/logo.jpg’

master_FINAL.py- name of most recent update of script
400- the number of photos that you want filtered
‘http://APIROOT‘ - root of the API call
's3://HACKREACTOR/can.jpg’- location of the first template
‘s3://HACKREACTOR/logo.jpg’- location of the second template