PIXLEE
======
PIXLEE Computer Vision System

The purpose of this project is to provide PIXLEE with a system that will take a template, and filter photos from a clients social media stream by that template.  The example data used for this system is from Coke, and the templates used to filter were a picture of a can, and a picture of the coke logo.  A visualization of the original and filtered images was created by Greg Palmer- https://github.com/g-palmer/, and is viewable at http://computer-vision-example-pixlee.nodejitsu.com/.

PIXLEE provides technologies that enable clients to collect, display and measure user-generated photos, as well as leverage their photos to drive traffic and increase sales.  Currently photos are filtered manually, and PIXLEE has no methodology to automatically select images that contain a certain image.  I developed a script that does this, and uploaded it to a ubuntu server connected to S3 buckets that allow for easy access to templates, and export of filtered photos.       

Filtering Process-

1. Upload template to be filtered to S3
2. Enter command line inputs on EC2 Ubuntu server
3. Retrieve JSON objects from API
4. Convert to CSV (later used to score photos that contain the template)
5. Retrieve photos and store to server
6. Analyze photos
7. Output filtered photos to S3, scored data to CSV file

Command Line Inputs-

python master_FINAL.py 400 ‘http://api.pixlee.com/v1XVC/HackXXX/albumsX/1230?api_key=SPsSUXOeT6jlQgGXw1de7qT2&pXerTpage=100@page=‘ 's3://PIXLEE_HACKREACTOR/can.jpg’ ‘s3://PIXLEE_HACKREACTOR/logo.jpg’

1. master_FINAL.py- name of most recent update of script
2. 400- the number of photos that you want filtered
3. ‘http://api.pixlee.com/v1XVC/HackXXX/albumsX/1230?api_key=SPsSUXOeT6jlQgGXw1de7qT2&pXerTpage=100@page=‘ - root of the API call
4. 's3://PIXLEE_HACKREACTOR/can.jpg’- location of the first template
5. ‘s3://PIXLEE_HACKREACTOR/logo.jpg’- location of the second template
