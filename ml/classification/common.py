"""
This image classification project works on data in the MNIST format.
These are 28x28 px images. This project uses the pixels as features
to make classifications.

The traditional MNIST dataset contains images of handwritten digits 0-9.
The fashion adaptation contains images of ten different garment types.

Datasets:
- MNIST Digits:      https://yann.lecun.org/exdb/mnist/index.html
- MNIST Fashion:     https://github.com/zalandoresearch/fashion-mnist?tab=readme-ov-file
"""

import time

from PIL import Image
import numpy as np

###################
# ADJUSTABLE PARAMS
###################
# Dataset can be 'mnist' or 'fashion-mnist'
DATASET = 'fashion-mnist'

# Num images to use, can set to None to use all images (accurate, but slow).
# KNN is a lazy learning algorithm that trains at the same time it tests,
#  which unfortunately makes is very slow if there is too much training data.
TRAINING_DATA_SIZE = 10_000  # num images to use for training.
TESTING_DATA_SIZE = 100  # num images to use for testing.

###################
# REST OF CODE
###################
def read_png(filepath):
    return np.asarray(Image.open(filepath).convert("L"))

def write_png(image, filepath):
    """
    Write PNG file from a 2D array of integers (image).
    The 2D array is converted to a 2D NumPy array of unsigned bytes (uint8) (0-255).
    All values in the image should be between 0-255, so there is no loss.
    """
    np_arr = np.array(image, dtype=np.uint8)
    im = Image.fromarray(np_arr)
    im.save(filepath)

def bytes_to_int(b):
    return int.from_bytes(b, byteorder="big")


def read_images(filename, max_num_images=None):
    """
    Read images file, return list of images.
    1 image = list of rows. 1 row = list of pixel values

    Pixel values are unsigned byte/unit8.
    These are 0-255 values. According to MNIST file format, 0 is white and 255
    is black. HOWEVER, PIL treats 0 as black and 255 as white, so we apply an
    inversion before returning.

    MNIST file format: https://yann.lecun.org/exdb/mnist/index.html
    """
    images = []
    with open(file=filename, mode="rb") as f:
        # ignore magic number
        f.read(4)
        num_images = bytes_to_int(f.read(4))
        num_rows = bytes_to_int(f.read(4))
        num_cols = bytes_to_int(f.read(4))

        if max_num_images:
            num_images = min(num_images, max_num_images)

        for image_idx in range(num_images):
            image = []
            for row in range(num_rows):
                image_row = []
                for col in range(num_cols):
                    pixel = bytes_to_int(f.read(1))
                    flip_pixel = abs(255 - pixel)
                    image_row.append(flip_pixel)
                image.append(image_row)
            images.append(image)
    return images


def read_labels(filename, max_num_labels=None):
    """
    Read labels file, return list of labels.
    1 label = integer 0-9 or a string retrieved from get_label.
    MNIST file format: https://yann.lecun.org/exdb/mnist/index.html
    """
    labels = []
    with open(file=filename, mode="rb") as f:
        # ignore magic number
        f.read(4)
        num_labels = bytes_to_int(f.read(4))

        if max_num_labels:
            num_labels = min(num_labels, max_num_labels)

        for label_idx in range(num_labels):
            label = bytes_to_int(f.read(1))
            labels.append(get_label(label))
    return labels


def get_label(idx):
    """
    Get label that corresponds to 0-9.
    For mnist dataset, return 0-9 (integer).
    For fashion-mnist dataset, return corresponding garment (string).
    """
    if DATASET == 'mnist':
        return idx
    elif DATASET == 'fashion-mnist':
        return [
            "T-shirt/top",  # 0
            "Trouser",
            "Pullover",  # 2
            "Dress",
            "Coat",  # 4
            "Sandal",
            "Shirt",  # 6
            "Sneaker",
            "Bag",  # 8
            "Ankle boot",
        ][idx]
    else:
        raise RuntimeError(f"Unrecognized dataset: {DATASET}")


def flatten_list(l):
    """ Flatten a list of lists. 2D -> 1D. """
    return [item for sublist in l for item in sublist]


def extract_features(X):
    """
    Extract features from images, by flattening each image.
    So instead of a list of rows of pixel values, we have a single list of pixel values.
    Each pixel value is a feature.
    Feature vectors are 1D arrays.
    """
    return [flatten_list(image) for image in X]


def dist(image1, image2):
    return sum([
        (image1_px - image2_px) ** 2 for image1_px, image2_px in zip(image1, image2)
    ]) ** 0.5


def get_distances_for_image(X_train, x_test):
    """
    Given training data (X_train) and a single test image (x_test),
    return list of distances from the test image to each training image.
    """
    return [dist(x_train, x_test) for x_train in X_train]


def get_most_frequent_element(l):
    """Get most frequently occurring item in list"""
    return max(l, key=l.count)

def print_results(y_pred, y_test, raw_X_test, start_time=None, model="Not specified"):
    """
    Print results and accuracy of predicted labels (y_pred), given real
    labels (y_test).

    Also, pass in image arrays (raw_X_test) so we can write .png files in
    DEBUG mode.

    Lastly, pass in start_time to print the total run time of the file.
    """
    to_print = (f"DATASET:  {DATASET}"
                f"\nTRAINING_DATA_SIZE: {TRAINING_DATA_SIZE}"
                f"\nTESTING_DATA_SIZE:  {TESTING_DATA_SIZE}"
                f"\nMODEL: {model}")

    results = ""
    num_correct = 0
    for idx, (pred, expected) in enumerate(zip(y_pred, y_test)):
        correct = pred == expected
        results += f"\n({idx:4}) {correct:5} {f'PREDICTION: {pred}   EXPECTED: {expected}' if not correct else ''}"
        if correct:
            num_correct += 1
        else:
            write_png(raw_X_test[idx], f"{IMG_DIR}/{idx}.png")
    to_print += f"\n\nACCURACY: {num_correct / len(y_pred)}"

    if start_time:
        end_time = int(time.time())
        run_time = end_time - start_time
        to_print += f"\nRUNTIME: {run_time // 60:02}:{run_time % 60:02}"

    # Detailed results
    to_print += f"\n\n IDX  PASS"
    to_print += results

    with open(f"logs/{DATASET}_{TRAINING_DATA_SIZE}_{TESTING_DATA_SIZE}_{model}.log", "w") as f:
        print(to_print, file=f)

# Static filepaths
DATA_DIR = "data"
IMG_DIR = f"img/{DATASET}"
TEST_DATA_FILENAME = "/".join([DATA_DIR, DATASET, "t10k-images-idx3-ubyte"])
TEST_LABELS_FILENAME = "/".join([DATA_DIR, DATASET, "t10k-labels-idx1-ubyte"])
TRAIN_DATA_FILENAME = "/".join([DATA_DIR, DATASET, "train-images-idx3-ubyte"])
TRAIN_LABELS_FILENAME = "/".join([DATA_DIR, DATASET, "train-labels-idx1-ubyte"])

# Testing and training data for the main scripts to import.
raw_X_train = read_images(TRAIN_DATA_FILENAME, TRAINING_DATA_SIZE)
y_train     = read_labels(TRAIN_LABELS_FILENAME, TRAINING_DATA_SIZE)
raw_X_test  = read_images(TEST_DATA_FILENAME, TESTING_DATA_SIZE)
y_test      = read_labels(TEST_LABELS_FILENAME, TESTING_DATA_SIZE)

# Extract features
X_train = extract_features(raw_X_train)
X_test  = extract_features(raw_X_test)
