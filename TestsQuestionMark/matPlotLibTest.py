#Billy Tobin
#TestWithMatPlotLib
import json
import matplotlib.pyplot as plt
import numpy as np

from github import Github
import subprocess
import shutil
import os

x_axis = []
y_axis = []


f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\CurrentResult.txt")

data = json.load(f)

y_axis.append(data["Project Wide Statistics"]['percentage of overloaded'])
x_axis.append(data["Project Wide Statistics"]['Commit Number'])

for i in range(1,4):
    f = open("C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\Result"+str(i)+".txt")

    data = json.load(f)

    y_axis.append(data["Project Wide Statistics"]['percentage of overloaded'])
    x_axis.append(data["Project Wide Statistics"]['Commit Number'])

    #print(data["Project Wide Statistics"]['percentage of overloaded'])
    




#fig, ax = plt.subplots()
x_axis.reverse()
plt.plot(x_axis, y_axis)
plt.xlabel('Commits ago -- (Older to Newer)')  # Add an x-label to the axes.
plt.ylabel('Percentage of Overloaded Methods')
plt.title("RxJava")  # Add a title to the axes.
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\Results1.2\\RxJava\\graph.png')
plt.savefig('C:\\Users\\willi\\Summer-Work21\\Results\\RxJava.png')
#plt.show()