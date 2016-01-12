# COPS-COP

Installation du client COP :

régler locales
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install cmake
sudo apt-get install python-dev
sudo apt-get install python-dev
sudo apt-get install python-zbar
sudo apt-get install python-qrtools
sudo pip install sqlalchemy
sudo apt-get install mysql-server --fix-missing
sudo apt-get install python-mysqldb

git clone https://github.com/raspberrypi/userland.git
cd userland
./buildme
git clone https://github.com/ashtons/picam.git
cd picam
sudo python setup.py install
sudo apt-get install rpi-update
sudo rpi-update


git clone https://github.com/Maxsky5/COPS-COP.git
cd COPS-COP

creer un bash_alias qui positionne le python path au démarrage
export PYTHONPATH="${PYTHONPATH}:/path/to/COPS-COP
ajouter ce bash_alias au bashrc de l'utilisateur courrant
