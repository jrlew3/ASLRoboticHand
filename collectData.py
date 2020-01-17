import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier

MEASURESIZE = 10
STEPSIZE = 8

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
            a = np.array(l[STEPSIZE*i:min(STEPSIZE*i + MEASURESIZE, len(l))], dtype=np.float128)
            agg = np.concatenate((np.mean(a, axis=0), np.std(a, axis=0)))
            ch = clf.predict(agg.reshape(1, -1))[0]
            prob = clf.predict_proba(agg.reshape(1, -1))[0]
            if True in np.isnan(prob):
                continue
            if ch != prevchar:
                prevchar = ch
                print(ch)
                #print(clf.predict_proba(agg.reshape(1, -1)))
    print("")

def trainer(folder):
    for i in range(0,26):
        if i == 9 or i == 25:
            continue
        filename = 'data/{}/train_{}.csv'.format(folder, chr(i + 97))
        train(filename, chr(i + 97))


train('data/visualizer/train_a.csv','a')
'''
train('data/visualizer/train_b.csv','b')
train('data/visualizer/train_c.csv','c')
'''
train('data/visualizer/train_i.csv','i')
train('data/visualizer/train_y.csv','y')
'''
train('data/visualizer/train_m.csv','y')
train('data/visualizer/train_n.csv','y')
train('data/visualizer/train_t.csv','y')
'''

clf = LinearDiscriminantAnalysis()
#clf = MLPClassifier()
clf.fit(X, y)

test('data/visualizer/test_a.csv')
'''
test('data/visualizer/test_b.csv')
test('data/visualizer/test_c.csv')
'''
test('data/visualizer/test_i.csv')
test('data/visualizer/test_y.csv')
'''
test('data/visualizer/test_t.csv')
test('data/p3/train_a.csv')
test('data/p3/train_b.csv')
test('data/p3/train_c.csv')
test('data/p3/train_d.csv')
test('data/p3/train_e.csv')
test('data/p3/train_f.csv')
test('data/p3/train_g.csv')
test('data/p3/train_h.csv')
test('data/p3/train_i.csv')
test('data/p3/train_j.csv')
test('data/p3/train_k.csv')
test('data/p3/train_l.csv')
test('data/p3/train_m.csv')
test('data/p3/train_n.csv')
test('data/p3/train_o.csv')
test('data/p3/train_p.csv')
test('data/p3/train_q.csv')
test('data/p3/train_r.csv')
test('data/p3/train_s.csv')
test('data/p3/train_t.csv')
test('data/p3/train_u.csv')
test('data/p3/train_v.csv')
test('data/p3/train_w.csv')
test('data/p3/train_x.csv')
test('data/p3/train_y.csv')
test('data/p3/train_z.csv')
'''





