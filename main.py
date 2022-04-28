import time
from calculator import *
import requestMaker
import tkinter as tk
from tkinter import filedialog, Text
import os



c = requestMaker.RequestMaker("https://www.escapefromtarkov.com/cash","div","count_left")

changes = []
left = []
while True:
    if len(left) == 0:
        left.append(c.getCurent())
    else:
        if len(left) >= 120:
            left = left[1:120]
            left.append(c.getCurent())
        else:
            left.append(c.getCurent())
        if len(changes) >= 10:
            changes = changes[1:120]
            changes.append(left[len(left) - 2] - left[len(left) - 1])
        else:
            changes.append(left[len(left) - 2] - left[len(left) - 1])
    if len(changes):
        print("Current estimate:",liveCalc(c.getCurent(),changes[len(changes)-1]))
    if len(changes) >= 5:
        print("5 Minit Estimate:", calc5Min(c.getCurent(), changes[len(changes)-5:]))
    if len(changes) >= 10:
        print("10 Minit Estimate:",calc10Min(c.getCurent(),changes[len(changes)-10:]))
    if len(changes) >= 30:
        print("30 Minit Estimate:",calc30Min(c.getCurent(),changes[len(changes)-30]))
    if len(changes) >= 60:
        print("60 Minit Estimate:",calc60Min(c.getCurent(),changes[len(changes)-60:]))


    time.sleep(60)
