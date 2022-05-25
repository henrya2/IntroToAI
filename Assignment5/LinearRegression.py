# CS480 Assignment 5 - Linear Regression using Normal Equation

# import required packages
import matplotlib.pyplot as plt     # for any plotting methods. Optional usage
import numpy as np                  # to do matrix computations / linear algebra
from sklearn import datasets        # to import datasets
from sklearn.model_selection import train_test_split        # to split train and test datasets


def print_student_name_Anumber():
    """
    Method to print student name and Anumber
    Args: None
    Returns : None
    """
    # TODO
    print("Student full name :", "XYS")  # replace XYS with your name
    print("Student A Number :", " A123456")  # replace with your A Number


class DataLoader:
    # class to load datasets

    def load_data(self):
        """
        Method to load Boston Housing dataset
        Args: None
        Returns :
            X (ndarray): An N-dimensional array of features
            y (ndarray): An N-dimensional array of target values
        """
        # already done
        X, y = datasets.load_boston(return_X_y=True)
        return X, y

    def split_train_test(self, X, y):
        """
        Method to split train and test set
        Args:
            X (ndarray): An N-dimensional array of features
            y (ndarray): An N-dimensional array of target values
        Returns :
            X_train (ndarray): An N-dimensional array of training features
            X_test (ndarray): An N-dimensional array of testing features
            y_train (ndarray): An N-dimensional array of training target values
            y_test (ndarray): An N-dimensional array of test target values
        """
        # already done
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
        return X_train, X_test, y_train, y_test


class LinearRegression:
    # class to implement linear regression
    def __init__(self):
        """
        Constructor for the class
        Args: None
        Returns : None
        """
        # already done
        # initialize weights as empty matrix
        self.W = []

    def fit(self, X, y):
        """
        Method to train the linear regression model
        Args:
            X (ndarray): Input training features
            y (ndarray): Input training target values
        Returns : None
        """
        # find W.
        # TODO
        m = X.shape[0]
        # Appends a column of ones to X for the bias term.
        one_arr = np.ones((m, 1))
        X = np.hstack((one_arr, X))

        # Reshapes y to (m, 1)
        y = y.reshape(m, 1)

        # The Normal Equation for linear regression
        self.W = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))



    def predict(self, X):
        """
        Method for prediction using the linear regression model
        Args:
            X (ndarray): Test features
        Returns :
            y_pred (ndarray): Predicted y' values
        """
        # find y_pred
        # TODO
        m = X.shape[0]

        # Appends a column of ones to X for the bias term.
        one_arr = np.ones((m, 1))
        X = np.hstack((one_arr, X))

        # Do the prediction dot product
        y_pred = np.dot(X, self.W)

        # Reshape y_pred to (m) which match the original shape of y
        y_pred = y_pred.reshape(m)

        return y_pred



    def loss(self, y_test, y_pred):
        """
        Method for calculate mean squared error
        Args:
            y_pred (ndarray): Ground truth values
            y_test (ndarray): Predicted values
        Returns :
            mse (float): MSE
        """
        # calculate mse
        # TODO
        mse = np.square(y_pred - y_test).mean()

        return mse


def main():
    """
    Main function which calls other methods

    :return:
    """
    print_student_name_Anumber()
    D = DataLoader()
    X, y = D.load_data()
    # TODO : Feel free to understand the data here, if needed
    X_train, X_test, y_train, y_test = D.split_train_test(X, y)
    # TODO Fit, predict and evaluate using linear regression model
    my_linear_model = LinearRegression()
    my_linear_model.fit(X_train, y_train)
    y_predict = my_linear_model.predict(X_test)
    mse = my_linear_model.loss(y_test, y_predict)

    print("Mean Squared Error = ", mse)


if __name__ =='__main__':
    main()