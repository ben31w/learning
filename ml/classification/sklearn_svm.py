"""Image classification with Support Vector Machine model from SKLearn."""

from common import X_train, y_train, X_test, y_test, raw_X_test, print_results

import time

from sklearn.svm import SVC


def main():
    start_time = int(time.time())

    # Use SVM to make predictions
    model = SVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print_results(y_pred, y_test, raw_X_test, start_time, "SVM")


if __name__ == '__main__':
    main()

