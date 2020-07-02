import csv
import os

import numpy as np
from PIL import Image

_index = 0
_output_dir = '../../output/'


def state_list_to_image(epoch, reward, steps, map_filepath, output_dir='../output/'):
    image = np.array(Image.open(map_filepath))
    output_image_dir = '{}/{}/'.format(output_dir, epoch)
    if not os.path.exists(output_image_dir):
        os.mkdir(output_image_dir)

    print(os.getcwd())
    with open('{}/state_list_{}_{:.0f}_{}.csv'.format(output_dir, epoch, reward, steps), 'r') as input_state_list:
        input_csv = csv.reader(input_state_list)
        state_list = []
        for line in input_csv:
            state_list.append(line)
        state_list = state_list[0]

    print(state_list)
    for i, state in enumerate(state_list):
        state = int(state)
        img = image.copy()
        x = state % 50
        y = int(state / 50)
        img[y, x] = [0, 255, 255, 255]
        img = Image.fromarray(img)
        img.save('{}{}.png'.format(output_image_dir, i))
