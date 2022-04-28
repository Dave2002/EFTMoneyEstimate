
def liveCalc(last,div):
    return (last/div)/60

def calcCustomMin(last,changes):
    return (last/(sum(changes)/len(changes)))/60
