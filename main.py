import time
from calculator import *
import requestMaker




c = requestMaker.RequestMaker("https://www.escapefromtarkov.com/cash","div","count_left")

changes = []
left = []
while True:
    if len(left) == 0:
        left.append(c.getCurent())
    else:
        if len(left) >= 600:
            left = left[1:600]
            left.append(c.getCurent())
        else:
            left.append(c.getCurent())
        if len(changes) >= 600:
            changes = changes[1:600]
            changes.append(left[len(left) - 2] - left[len(left) - 1])
        else:
            changes.append(left[len(left) - 2] - left[len(left) - 1])
    if len(changes):
        print("Current estimate:",liveCalc(c.getCurent(),changes[len(changes)-1]))
    if len(changes) >= 5:
        print("5 Minit Estimate:", calcCustomMin(c.getCurent(),changes[len(changes)-5:]))
    if len(changes) >= 10:
        print("10 Minit Estimate:",calcCustomMin(c.getCurent(),changes[len(changes)-10:]))
    if len(changes) >= 30:
        print("30 Minit Estimate:",calcCustomMin(c.getCurent(),changes[len(changes)-30]))
    if len(changes) >= 60:
        print("60 Minit Estimate:",calcCustomMin(c.getCurent(),changes[len(changes)-60:]))
    if len(changes) >= 120:
        print("120 Minit Estimate:",calcCustomMin(c.getCurent(),changes[len(changes)-120:]))
    if len(changes) >= 240:
        print("240 Minit Estimate:",calcCustomMin(c.getCurent(),changes[len(changes)-240:]))
    if len(changes) >= 480:
        print("480 Minit Estimate:",calcCustomMin(c.getCurent(),changes[len(changes)-480:]))

    time.sleep(60)
