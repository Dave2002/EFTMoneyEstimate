
def liveCalc(last,div):
    return (last/div)/60

def calc5Min(last,change5):
    return (last/(sum(change5)/len(change5)))/60

def calc10Min(last,change10):
    return (last/(sum(change10)/len(change10)))/60

def calc30Min(last,change30):
    return (last/(sum(change30)/len(change30)))/60

def calc60Min(last,change60):
    return (last/(sum(change60)/len(change60)))/60