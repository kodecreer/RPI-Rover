sudo apt-get update
sudo apt-get upgrade
echo 'os updated' 

sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev 
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev 
sudo apt-get install libgtk2.0-dev libgtk-3-dev 
sudo apt-get install libatlas-base-dev gfortran 

sudo apt-get install python3-dev
sudo apt-get install python3-pip 
echo 'installing the dependacies are done'

pip3 install opencv-python 

sudo apt-get install libqtgui4
sudo modprobe bcm2835-v4l2
sudo apt-get install libqt4-test

