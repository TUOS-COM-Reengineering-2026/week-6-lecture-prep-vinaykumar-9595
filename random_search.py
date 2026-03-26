import numpy as np
from lecture import complex_math

def random_search(function, num_samples=1000, bounds=(-100, 100)):
    best_x, best_y = None, None
    best_output = float('inf')

    for _ in range(num_samples):
        # Improved sampling: use continuous values
        x = np.random.uniform(bounds[0], bounds[1])
        y = np.random.uniform(bounds[0], bounds[1])

        value = function(x, y)

        if value < best_output:
            best_x, best_y, best_output = x, y, value

    return best_x, best_y, best_output


if __name__ == '__main__':
    x, y, v = random_search(function=complex_math)

    print(f"Best x: {x}")
    print(f"Best y: {y}")
    print(f"Best output: {v}")
