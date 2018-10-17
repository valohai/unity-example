import argparse
import glob
import json
import os
import random
import time

import numpy as np
import tensorflow as tf


def main(settings):

    # You can use any libraries in the Docker image or installed with pip.
    print('numpy', np.__version__)
    print('tensorflow', tf.__version__)

    # You can access the inputs at /valohai/inputs/<input_name>
    images_dir = os.path.join(settings.inputs_dir, 'images')
    image_count = len(glob.glob(os.path.join(images_dir, '*.png')))
    print('image count: {0}'.format(image_count))

    # Here you could do any pre-processing, training and validation.
    # We are just mocking something for simplicity.
    iterations = int(settings.epochs / 20)
    for i in range(0, iterations):
        epoch = (i + 1) * 20
        accuracy = random.random()
        print(json.dumps({'epoch': epoch, 'accuracy': accuracy}))
        time.sleep(0.5)

    # You can store anything writing it to /valohai/outputs
    # Here we are are writing some mock numbers to CSV files but
    # outputs can be anything e.g. HDF5-files, images, audion, video.
    print('writing weights and biases...')
    weights_path = os.path.join(settings.outputs_dir, 'model-weights.csv')
    with open(weights_path, 'w') as f:
        weights_list = [random.random() for _ in range(100)]
        weights_str = ', '.join(map(str, weights_list))
        f.write(weights_str)

    biases_path = os.path.join(settings.outputs_dir, 'model-biases.csv')
    with open(biases_path, 'w') as f:
        biases_list = [random.random() for _ in range(100)]
        biases_str = ', '.join(map(str, biases_list))
        f.write(biases_str)
    print('done writing weights and biases')

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs_dir', type=str, default=os.getenv('VH_INPUTS_DIR', './inputs'))
    parser.add_argument('--outputs_dir', type=str, default=os.getenv('VH_OUTPUTS_DIR', './outputs'))
    parser.add_argument('--epochs', type=int, default=200)
    settings = parser.parse_args()
    main(settings)


if __name__ == "__main__":
    cli()
