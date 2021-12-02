sudo apt update -y
sudo apt full-upgrade -y
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
sudo i2cdetect -y 1
pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil

 
