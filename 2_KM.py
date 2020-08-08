import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

TOL = 0.001
ITER = 30
CLUSTER = 3

class K_Means:
    def __init__(self, k=CLUSTER, tol=TOL, max_iter=ITER):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):
        self.centroids = {}

        # intializing the centroids to 1st 3 ele
        for i in range(self.k):
            self.centroids[i] = data[i]
            print(self.centroids)

        # iterate for max _iterations
        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            # create cluster & cal Euclidean distance
            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            # recal mean/centroid
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            
            optimized = True

            # check for tolerance
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroi = self.centroids[c]
                if np.sum((current_centroi - original_centroid) / original_centroid * 100.0) > self.tol:
                    print("New centroid :: " , np.sum((current_centroi - original_centroid) / original_centroid * 100.0))
                    optimized = False

            if optimized:
                break


    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroif in self.centroids]
        classification = distances.index(min(distances))
        return classification


############################################################
# Driver code
# Reading the first 2 cols of the dataset
X = pd.read_csv("iris.csv", header = None, usecols = [0, 1, 2, 3])
colors = ['r', 'g', 'b', 'c', 'k', 'o', 'y']

clf = K_Means()
clf.fit(np.array(X))

for i in range(150):
    plt.scatter(np.array(X)[i][0], np.array(X)[i][1], 
    color="r", marker="*")
plt.show()

for centroid in clf.centroids:
    print(clf.centroids[centroid][0], " ", clf.centroids[centroid][1])
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="*", color="k", s=150, linewidths=5)
    
for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1],
                    marker="2", color=color, s=150, linewidths=5)

plt.show()