import sys
import importlib
import argparse
import numpy as np
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--SRN', required=True)
parser.add_argument('--verbose', default = 0 )
parser.add_argument('--k_neigh', default = 2)


args = parser.parse_args()
subname = args.SRN
verbose = True if args.verbose=="1" else False
k_neigh = int(args.k_neigh)

try:
    mymodule = importlib.import_module(subname)
except Exception as e:
    print(e)
    print("Rename your written program as YOUR_SRN.py and run python3.7 SampleTest.py --SRN YOUR_SRN ")
    sys.exit()

KNN = mymodule.KNN
FILENAME = "./iris.csv"
df = pd.read_csv(FILENAME)
dfX = pd.DataFrame(df, columns=["sepal.length", "sepal.width", "petal.length", "petal.width"])
dfY = pd.DataFrame(df, columns=["variety"])
X = np.array(dfX, dtype=float)
y = np.array(dfY)
encoding = {}
start = 0
y2 = []
for i in y:
    ke = i[0]
    if ke in encoding:
        y2.append(encoding[ke])
    else:
        encoding[ke] = start
        start += 1
        y2.append(encoding[ke])
y = np.array(y2)
train_X = X[:int(0.8*len(X))]
train_y = y[:int(0.8*len(y))]
test_X = X[int(0.8*len(X)):]
test_y = y[int(0.8*len(y)):]

model = KNN(k_neigh = k_neigh, p = 2)
model.fit(train_X, train_y)

print("Un-Wegihted idk what the opposite of weighted is:")
if (verbose == True):
    print("Find_distance:\n", model.find_distance(test_X))
    print("-"*45)
    print("\n")
if (verbose == True):
    print("k_neighbours:\n", model.k_neighbours(test_X))
    print("-"*45)
    print("\n")
if (verbose == True):
    print("predict:\n", model.predict(test_X))
    print("-"*45)
    print("\n")

print("Evaluate: ", model.evaluate(test_X, test_y))
print("\n\n")

modelW = KNN(k_neigh = k_neigh, weighted=True, p = 2)
modelW.fit(train_X, train_y)

print("Wegihted:")
if (verbose == True):
    print("Find_distance:\n", modelW.find_distance(test_X))
    print("-"*45)
    print("\n")
if (verbose == True):
    print("k_neighbours:\n", modelW.k_neighbours(test_X))
    print("-"*45)
    print("\n")
if (verbose == True):
    print("predict:\n", modelW.predict(test_X))
    print("-"*45)
    print("\n")

print("Evaluate: ", modelW.evaluate(test_X, test_y))
print("\n\n")
