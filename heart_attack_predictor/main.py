from neural_network.layers import Dense
from neural_network.models import Sequential
from neural_network.model_selection import KFold, train_test_split
from neural_network.metrics import confusion_matrix, accuracy_score, accuracy_by_label
from neural_network.preprocess import OneHotEncoder
import numpy as np
from data import load_data

X, y = load_data()
print(X.shape)
print(y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

labels = np.unique(y)
encoder = OneHotEncoder().fit(labels)
y_train = encoder.transform(y_train)
y_test = encoder.transform(y_test)

net = Sequential()

net.add(
    Dense(64, input_shape=11, activation='tanh'),
    Dense(64, activation='tanh'),
    Dense(2, activation='sigmoid')
)

net.compile(cost='mse', metrics=[
            'accuracy_score'])

kf = KFold(n_splits=5)

for train, validate in kf.split(X_train):
    net.fit(
        X_train[train],
        y_train[train],
        epochs=10,
        validation_data=(X_train[validate], y_train[validate])
    )


predictions = net.predict(X_test, classify=True)
print()
print(confusion_matrix(y_test, predictions))
print()
print(accuracy_score(y_test, predictions))
print()
print(accuracy_by_label(y_test, predictions))
