"""
Image classification from scratch using k-Nearest Neighbors (KNN).
Tutorial: https://www.youtube.com/watch?v=vzabeKdW9tE
"""

from common import (X_train, y_train, X_test, y_test, raw_X_test, print_results,
                    get_distances_for_image, get_most_frequent_element)
import time


def knn(X_train, y_train, X_test, k=3):
    """ 
    k-Nearest Neighbors algorithm. 
    Given training data (X_train), training labels (y_train), and test data (X_test),
    predict labels for test data using k-NN with k neighbors.
    """
    y_pred = []  # predicted labels for test data
    idx = 0  # only used for printing purposes, not really needed by KNN.
    for x_test in X_test:
        distances = get_distances_for_image(X_train, x_test)
        # get indices of images within X_train, sorted so that images with the
        #   least distance with x_test are first.
        sorted_distance_indices = [
            pair[0] for pair in sorted(enumerate(distances), key=lambda x: x[1])
        ]
        k_indices = sorted_distance_indices[:k]
        k_labels = [y_train[i] for i in k_indices]
        print(f"({idx:4}) {k} nearest neighbors are {k_labels}")
        idx += 1

        pred = get_most_frequent_element(k_labels)
        y_pred.append(pred)

    return y_pred


def main():
    start_time = int(time.time())

    # Use KNN to make predictions
    y_pred = knn(X_train, y_train, X_test, k=3)

    print_results(y_pred, y_test, raw_X_test, start_time)


if __name__ == "__main__":
    main()
