import argparse
import os
import numpy as np
import tensorflow as tf

def main(settings):

    # You can use any libraries in the Docker image or installed with pip.
    print('numpy', np.__version__)
    print('tensorflow', tf.__version__)

    # You can access the inputs at /valohai/inputs/<input_name>
    images_dir = os.path.join(settings.inputs_dir, 'images')
    try:
        print(os.listdir(images_dir))
    except FileNotFoundError:
        print('input image directory not found')
        pass

    # Here you do any computation.

    # You can store anything writing it to /valohai/outputs
    print(settings.outputs_dir)

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs_dir', type=str, default=os.getenv('VH_INPUTS_DIR', './inputs'))
    parser.add_argument('--outputs_dir', type=str, default=os.getenv('VH_OUTPUTS_DIR', './outputs'))
    settings = parser.parse_args()
    main(settings)

if __name__ == "__main__":
    cli()
