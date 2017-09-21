# OpenCV MapMyIndia project

[![N|Solid](https://avatars3.githubusercontent.com/u/5009934)](https://ashishtaldeokar.in)

This project is for MapMyIndia, the problem statement assigned is as follows.

    Map companies collects terrestrial image data using Land Mobile Mapping Systems to provide services like 360 deg Virtual tour (eg: Google's StreetView). Privacy is of paramount concern when this data is published over internet, therefore it's necessary to mask/blurr the identiy informations like human faces and vechile number plates from the collected images before they can be published over internet. To alleviate these concerns, your task as an employee of MapMyIndia is to use supervised learning techniques to construct a demonstation of a face identification and vehicle number plate identification in offline mode. Also, report the accuracy of identifications of face and vehicle number plate.

# Naive Approach

  - Using openCV classifiers detect coordinates of faces and numberplates.
  - replace these patches of image with a gaussian blur of itself
  - IMP: there are two different classifiers i.e.
        * FACE 
        * NUMBER PLATES


TODO:
  - Replace the haarcascade classifiers with ConvNet classifiers
  - Here too, there will be two different classifiers as naive approach
  - Improve function for scalability
 
### Run the code

This code requires [Python](https://www.python.org/download/releases/3.0/) v3.6+ to run.

Install the dependencies.

```sh
$ pip install -r requirements.txt
$ python mapmyindia.py
```
License
----

MIT


**Free Software, Hell Yeah!**
