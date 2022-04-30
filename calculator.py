
def liveCalc(last,div):
    try:
        return (last/div)/60
    except:
        return "error"

def calcCustomMin(last,changes):
    try:
        return (last/(sum(changes)/len(changes)))/60
    except:
        return "errort"