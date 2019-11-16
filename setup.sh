sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3-rpi.gpio
sudo apt install python3-psutil
sudo apt install python3-flask
sudo apt install gcc make build-essential python3-dev git scons swig
sudo echo "\nblacklist snd_bcm2835\n"  >> /etc/modprobe.d/snd-blacklist.conf