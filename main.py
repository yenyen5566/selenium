#!/usr/bin/python

import requests as r
from bs4 import BeautifulSoup
import time
import threading
from datetime import date
from selenium import webdriver
import sys
from function import *
import os

#os.system("Xvfb :54321 -ac &")

#os.system("export DISPLAY=:54321")

times = int(sys.argv[1])

number = int(sys.argv[2])

sol_idea_test(times,number)


