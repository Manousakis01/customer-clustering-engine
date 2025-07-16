import numpy as np
from clustering import evaluate

def test_print_scores():
    X = np.random.rand(10, 2)
    labels = [0]*5 + [1]*5
    score = evaluate.print_scores(X, labels)
    assert isinstance(score, float)
