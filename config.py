import os


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
print(f"Root path: {BASE_PATH}")

IMAGES_PATH = os.path.join(BASE_PATH, 'dataset', 'images')
ANNOTS_PATH = os.path.join(BASE_PATH, 'dataset', 'annotations')

IMAGE_CATEGORIES = ["motorbike", "airplane"]

# output dir path
BASE_OUTPUT = os.path.join(BASE_PATH, 'output')

# define the path to the output model, label binarizer, plots output
# directory, and testing image paths
MODEL_PATH = os.path.join(BASE_OUTPUT, "detector.h5")
LB_PATH = os.path.join(BASE_OUTPUT, "lb.pickle")
PLOTS_PATH = os.path.join(BASE_OUTPUT, "plots")
TEST_PATHS = os.path.join(BASE_OUTPUT, "test_paths.txt")


INIT_LR = 1e-4 # initial learning rate
NUM_EPOCHS = 2 # number of epochs to train
BATCH_SIZE = 4 #32 # batch size