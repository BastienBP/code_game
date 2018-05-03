###OPENCV
brew install opencv
/usr/local/Cellar/opencv/3.4.1_4

#Get location of anaconda: 
#from distutils.sysconfig import get_python_lib
#print(get_python_lib())

cd /Users/$USER/anaconda2/lib/python2.7/site-packages

#

ln -s /usr/local/Cellar/opencv/3.4.1_4/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/3.4.1_4/lib/python2.7/site-packages/cv2.so cv2.so
