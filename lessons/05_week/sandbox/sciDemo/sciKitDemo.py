#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CS102F2022
# Regression Demonstration

# Modified by: Oliver Bonham-Carter
# Date: 25 Sept 2022


# Original code:
# License: BSD 3 clause
# Inspired from reference:
# https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#sphx-glr-download-auto-examples-ensemble-plot-adaboost-regression-py
# Author: Noel Dawe <noel.dawe@gmail.com>



import numpy as np

from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

import matplotlib.pyplot as plt
import seaborn as sns


def main():

    rng = np.random.RandomState(1)

    X = np.linspace(0, 6, 100)[:, np.newaxis]
    y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])

    regr_1 = DecisionTreeRegressor(max_depth=4)

    regr_2 = AdaBoostRegressor(
        DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
    )

    regr_1.fit(X, y)
    regr_2.fit(X, y)

    y_1 = regr_1.predict(X)
    y_2 = regr_2.predict(X)

    print(f"X={type(X)},y={type(y)},y_1 = {type(y_1)},y_2 = {type(y_2)}")
    plotter(X,y,y_1,y_2)
# end of main()


def plotter(X:list,y:list,y_1:list,y_2:list) -> None:
    """ function to plot parameter-inputted data"""
    colors = sns.color_palette("colorblind")
    plt.figure()
    plt.scatter(X, y, color=colors[0], label="training samples")
    plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
    plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Boosted Decision Tree Regression")
    plt.legend()
    fname = "regressionPlot.png"
    print(f"\t [+] Attempting to save to file {fname}")
    plt.savefig(fname)
    plt.show()
# end of plotter()

main()
