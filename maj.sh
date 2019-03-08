#! /bin/sh


rsync -avre ssh ./ pi:/home/pi/rp_gphoto2/ --exclude=".DS_Store"
