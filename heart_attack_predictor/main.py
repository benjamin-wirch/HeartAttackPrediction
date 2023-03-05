from data import load_data
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np


X, y = load_data()

X_train, X_test, y_train, y_test = train_test_split(X, y)

print(f'{len(X_train) = }')
print(f'{len(X_test) = }')
print(f'{len(y_train) = }')
print(f'{len(y_test) = }')

model = Sequential(
    [
        Dense(32, input_dim=11, activation='tanh'),
        Dense(64, activation='tanh'),
        Dense(16, activation='tanh'),
        Dense(1, activation='sigmoid'),
    ]
)

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100)

score = model.evaluate(X_test, y_test, verbose=0)
print("\nTest loss:", format(score[0c], ".4f"))
print("Test accuracy:", score[1])

# # Cell 8
# y_softmax = model.predict(X_test)

# y_pc = np.argmax(y_softmax, axis=-1)

# y_pred = to_categorical(y_pc)
