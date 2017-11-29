echo "Before this script runs, you must change the swapfile size. Open /etc/dphys-swapfile and edit the CONF_SWAPSIZE to be 1024.\n If you have not completed this step, press CTRL+C now to exit the script."

function pause(){
  read -p "$*"
}
echo "Otherwise press [ENTER] to continue."
pause

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3-dev
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
echo -e "\n# virtualenv and virtualwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs">> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
source ~/.profile
mkvirtualenv cv -p python3
source ~/.profile
workon cv
pip install numpy
workon cv
cd ~/opencv-3.3.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
      -D BUILD_EXAMPLES=ON

sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start

make -j4
sudo make install
sudo ldconfig

cd usr/local/lib/python3.5/site-packages/
sudo mv cv2.python-35m-arm-linux-gnueabihf.so cv2.so

cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3/5/site-packages/cv2.so cv2.so

echo "GREAT JOB! Now make sure to turn the swapfile size back to 100"
echo "Open another terminal window and complete this step. Then press [ENTER] in this window"
pause
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
