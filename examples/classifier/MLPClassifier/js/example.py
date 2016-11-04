from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.utils import shuffle

from onl.nok.sklearn.Porter import port

X, y = load_iris(return_X_y=True)

X = shuffle(X, random_state=0)
y = shuffle(y, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=5)

clf = MLPClassifier(
    activation='relu', hidden_layer_sizes=50, max_iter=500, alpha=1e-4,
    solver='sgd', tol=1e-4, random_state=1, learning_rate_init=.1)

clf.fit(X_train, y_train)

# Cheese!

print(port(clf, language='js'))

"""

"""
