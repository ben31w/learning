"""Image classification with Logistic Regression model from SKLearn."""

from common import X_train, y_train, X_test, y_test, raw_X_test, print_results

import time

from sklearn.linear_model import LogisticRegression


def main():
    start_time = int(time.time())

    # Use logistic regression to make predictions
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print_results(y_pred, y_test, raw_X_test, start_time, "LogisticRegression")


if __name__ == '__main__':
    main()

