import numpy as np


def load_data():
    arr = np.genfromtxt('./heart.csv', skip_header=True,
                        delimiter=',', dtype='int')
    return arr[:, :-1], arr[:, -1]


if __name__ == '__main__':
    print((a := load_data())[0], a[1], sep='\n')
