# commands

### to run on reboot (put at bottom of /etc/profile):

python3 /home/display1/working-slideshow.py OR python3 /home/display1/IEEE-slideshow-control/working-slideshow.py (if cloned)

### to edit files:

sudo nano /etc/profile

sudo nano working-slideshow.py OR sudo nano IEEE-slideshow-control/working-slideshow.py (if cloned)

### to install necessary packages (probably installed by default, run to check):

sudo apt-get install python3.9

sudo apt install python3-tk

pip install Pillow

sudo apt-get install git

### to clone this repo onto pi:

git clone https://github.com/ZachON5800/IEEE-slideshow-control (make sure you are connected to internet for this to work)

### if you get an ImportError resulting from the line "from PIL import ImageTk" in working-slideshow.py:

sudo apt-get install python3-pil python3-pil.imagetk

### installing teamviewer package:
wget https://download.teamviewer.com/download/linux/teamviewer-host_armhf.deb

--then--

sudo dpkg -i teamviewer-host_armhf.deb
