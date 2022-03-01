fname = input('Enter file: ')
if len(fname) < 1 : fname = 'hola.txt'
hand = open(fname)

di = dict()

for line in hand:
    line = line.rstrip()
    words = line.split()
    
    for w in words :
        # IDIOM: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

# encontrar la palabra mas comun
largest = -1
thewords = None
for key,value in di.items() :
    print(key,value)
    if value > largest :
        largest = value
        theword = key #capture/remember the word that was largest

print("done", theword,largest)