


X, y = load_data()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.1)

print(f'{len(X_train) = }')
print(f'{len(X_test) = }')
print(f'{len(y_train) = }')
print(f'{len(y_test) = }')


# model = create_model()
model = load_model('./outputdata.h5')

try:
    model.fit(X_train, y_train, epochs=5000)

except (KeyboardInterrupt, Exception):
    model.save('./outputdata.h5')
    print('Saved data')

score = model.evaluate(X_test, y_test, verbose=0)
print("\nTest loss:", format(score[0c], ".4f"))
print("Test accuracy:", score[1])

model.save('./outputdata.h5')
# # Cell 8
# y_softmax = model.predict(X_test)

# y_pc = np.argmax(y_softmax, axis=-1)

# y_pred = to_categorical(y_pc)
