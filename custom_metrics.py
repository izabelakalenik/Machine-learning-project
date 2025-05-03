import numpy as np

def relevance(y):
    return y / y.max()

def f_beta_regression(y_true, y_pred, beta=1.0, threshold=10):
    rel = relevance(y_true)
    TP = ((np.abs(y_true - y_pred) <= threshold) * rel).sum()
    FP = ((np.abs(y_true - y_pred) > threshold) * rel).sum()
    FN = ((np.abs(y_pred - y_true) > threshold) * rel).sum()

    precision = TP / (TP + FP + 1e-9)
    recall = TP / (TP + FN + 1e-9)

    beta2 = beta ** 2
    return (1 + beta2) * (precision * recall) / (beta2 * precision + recall + 1e-9)
