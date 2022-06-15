#Billy Tobin
#Cloning, analyzing, and making x projects
#
#
import json
import matplotlib.pyplot as plt
import numpy as np

from github import Github
import subprocess
import shutil
import os
from os import path
import sys
import time



### Change this 
##projectlist should be a list of repositories names, NAMES is important, they should be strings
projectlst = os.listdir(os.getcwd() + '\\Results\\Results5')




count = 0
project_list = []
url_list = []

for j in projectlst:
   
    ##Change this to your directory where you want the final analyses to be
    dir = "C:\\Users\\willi\\Summer-Work21\\Results\\CurrentAnalysis\\" + j
    if not os.path.exists(dir):
        os.mkdir(dir)

    ###Change this directory to where your repos are
    ##C:\\Users\\willi\\Summer-Work21\\currentRepos\\

    cmd = 'java -jar ck-0.6.5-SNAPSHOT-jar-with-dependencies.jar C:\\Users\\willi\\Summer-Work21\\currentRepos\\'+ j + ' False 0 False 0 '+ j+ " 0 0"
    pipe = subprocess.Popen(cmd, cwd='C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target')
    pipe.wait()

    shutil.move("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt", "C:\\Users\\willi\\Summer-Work21\\Results\\CurrentAnalysis\\" +j+"\\Result0.txt")
    #os.rmdir("C:\\Users\\willi\\Summer-Work21\\TestsQuestionMark\\ck\\target\\output.txt")

