import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

MEASURESIZE = 8
STEPSIZE = 4

X = []
y = []

def train(fname, cls):
    global X, y
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        #next(reader)
        l = []
        for row in reader:
            l.append([float(r) for r in row[2:]])
        for i in range(len(l) // STEPSIZE - 1):
            a = np.array(l[STEPSIZE*i:min(STEPSIZE*i + MEASURESIZE, len(l))])
            agg = np.concatenate((np.mean(a, axis=0), np.std(a, axis=0)))
            X.append(agg)
            y.append(cls)

def test(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        #next(reader)
        l = []
        for row in reader:
            l.append([float(r) for r in row[2:]])
        
        prevchar = -1
        for i in range(len(l) // STEPSIZE - 1):
            a = np.array(l[STEPSIZE*i:min(STEPSIZE*i + MEASURESIZE, len(l))])
            agg = np.concatenate((np.mean(a, axis=0), np.std(a, axis=0)))
            ch = clf.predict(agg.reshape(1, -1))[0]
            #if ch != prevchar:
            prevchar = ch
            print(ch)

'''
train('train1.csv', 1)
train('train2.csv', 2)
train('train3.csv', 3)'''
train('traina.csv', 'a')
train('testb.csv', 'b')
train('trainc.csv', 'c')


clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
'''
test('test1.csv')
print("")
test('test2.csv')
print("")
test('test1to2.csv')
print("")
test('test3.csv')
print("")
test('mysterytest.csv')
print("")'''
test('testa.csv')
print("")
test('trainb.csv')
print("")
test('testc.csv')
print("")
