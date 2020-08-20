import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

TOL = 0.001
ITER = 300
CLUSTER = 2


# random no generator for 2D array
def _random(bound, size):
    _rv = []
    _vis = []
    while True:
        r = np.random.randint(bound)
        if r in _vis:
            pass
        else:
            _vis.append(r)
            _rv.append(r)

        if len(_rv) == size:
            return _rv


class KMedoids:
    def __init__(self, k=CLUSTER, tol=TOL, max_iter=ITER):
        self.classifications = {}
        self.medoids = {}
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):

        _med = _random(len(data), self.k)

        for i in range(self.k):
            # taking random
            self.medoids[i] = data[_med[i]]

            # taking average
            # self.medoids[i] = np.average(data[i], axis=0)
            print(self.medoids[i])

        # iterate for max _iterations
        for i in range(self.max_iter):

            for i in range(self.k):
                self.classifications[i] = []

            # create cluster & cal Euclidean distance
            for featureset in data:
                distances = [np.linalg.norm(featureset - self.medoids[medoid]) for medoid in self.medoids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

    def predict(self, data):
        distances = [np.linalg.norm(data - self.medoids[medoid]) for medoid in self.medoids]
        classification = distances.index(min(distances))
        return classification


############################################################
# Driver code
# Reading the first 2 cols of the dataset
X = pd.read_csv("iris.csv", header=None, usecols=[0, 1, 2, 3])
colors = ['r', 'g', 'b', 'c', 'k', 'o', 'y']

clf = KMedoids()
clf.fit(np.array(X))

for i in range(150):
    plt.scatter(np.array(X)[i][0], np.array(X)[i][1],
                color="r", marker="*")
    plt.scatter(np.array(X)[i][2], np.array(X)[i][3],
                color="r", marker="*")

plt.xlabel("Sepal")
plt.ylabel("Petal")
plt.title("Iris Dataset")
plt.show()

# for sepals
for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1],
                    marker=".", color=color, linewidths=5)

for medoids in clf.medoids:
    plt.scatter(clf.medoids[medoids][0], clf.medoids[medoids][1],
                marker="*", color="b", s=100, linewidths=5)

plt.xlabel("Sepals Length")
plt.ylabel("Sepals Width")
plt.title("Sepals")
plt.show()

# for petals
for classification in clf.classifications:
    color = colors[classification]
    color1 = colors[classification + 1]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[2], featureset[3],
                    marker=".", color=color, linewidths=5)

for medoids in clf.medoids:
    plt.scatter(clf.medoids[medoids][2], clf.medoids[medoids][3],
                marker="*", color="b", s=100, linewidths=5)

plt.xlabel("Petals Length")
plt.ylabel("Petals Width")
plt.title("Petals")
plt.show()
