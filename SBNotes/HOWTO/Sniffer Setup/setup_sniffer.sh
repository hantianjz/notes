#!/bin/bash

sudo insmod /home/hjz/rtl8812AU/8812au.ko
sleep 1
sudo ip link set wlan1 up
sleep 1
sudo iwconfig wlan1 mode monitor
sleep 1

