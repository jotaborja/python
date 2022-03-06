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


#print(di)

tmp = list()
for k,v in di.items():
    #print(k,v)
    newtup = (v,k)
    tmp.append(newtup)

#print("flipped", tmp)

tmp = sorted(tmp, reverse=True)

#print("sorted", tmp)

for v,k in tmp[:5]:
    print(k,v)
