import numpy as np

class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tol:
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


if __name__ == '__main__':
    X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    clf = KMeans()
    clf.fit(X)
    print(clf.centroids)
    print(clf.classifications)
    print(clf.predict([0.1, 0.2]))

    # run clf with iris
    from sklearn.datasets import load_iris
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = KMeans(3)
    clf.fit(X)
    for centroid in clf.centroids:
        print(centroid)
        print(clf.centroids[centroid])
        print(clf.classifications[centroid])
        print()

    # visualize
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    colors = ["g.", "r.", "c.", "y."]
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[y[i]], markersize=10)
    plt.scatter(clf.centroids[0][0], clf.centroids[0][1], marker="x", s=150, linewidths=5, zorder=10)
    plt.scatter(clf.centroids[1][0], clf.centroids[1][1], marker="x", s=150, linewidths=5, zorder=10)
    plt.scatter(clf.centroids[2][0], clf.centroids[2][1], marker="x", s=150, linewidths=5, zorder=10)
    plt.show()
    



