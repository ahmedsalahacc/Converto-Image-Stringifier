import os
import argparse

import numpy as np
import matplotlib.pyplot as plt


from converto import ImageEncoder


def downGradeImageResolution(img: np.array, factor: int = 10) -> np.array:
    f'''
    Downgrades the image resolution by the given factor
    this operation is important to reduce the size of the output file
    (to make it more visible)

    Parameters
    ----------
    img : np.array of dimensions M x N (must be 2D)
        represents the input image
    factor: int Default=10
        represents the downgrade factor of the resolution

    Returns
    -------
    new_img : np.array
        represents the downgraded image by factor={factor}

    Notes
    -----
    It is adviced to play with the factor to keep the resolution of the 
    output image with in less than 180 x 180
    '''
    # check that the array is 2 dimensional
    assert(len(img.shape) == 2)

    h, w = img.shape
    new_img = []

    for y in range(0, h, factor):
        row = []
        for x in range(0, w, factor):
            row.append(img[y][x])
        new_img.append(row)

    new_img = np.array(new_img)

    return new_img


def quantize(img: np.array) -> np.array:
    '''
    Quantizes the image by converting the image
    from [0-1] scale to [0-255] scale

    Parameters
    ----------
    img: np.array representing the dequantized image

    Returns: np.array representing the quantized image
    '''
    # check that the array is 2 dimensional
    assert(len(img.shape) == 2)

    MAX_IMG_RESOLUTION = 2**8-1

    return np.floor(img*MAX_IMG_RESOLUTION)


def main():
    ''' main code goes here'''
    # directory of outputs
    cwd = os.getcwd()
    OUTPUT_DIR_PATH = os.path.join(cwd, 'outputs')
    if not os.path.isdir(OUTPUT_DIR_PATH):
        os.mkdir(OUTPUT_DIR_PATH)
    # parser
    FRINGE = 10
    IMG_FILE = "D:\\Images\\me1.png"
    RES_DOWNGRADE_FACTOR = 8
    OUT_IMG_FILE = os.path.join(OUTPUT_DIR_PATH, IMG_FILE.split('\\')[-1]
                                .split('.')[0]+'_encoded_out.txt')

    img = plt.imread(IMG_FILE)[:, :, 0]  # only deal with grayscale level
    print(img.shape)
    encoder = ImageEncoder(FRINGE)

    # downgrade image resolution
    down_graded_img = downGradeImageResolution(
        img, factor=RES_DOWNGRADE_FACTOR)

    # quantize image
    down_graded_img = quantize(down_graded_img)
    print(down_graded_img.shape)
    # converting image
    encoder.convertImage(down_graded_img, out_filename=OUT_IMG_FILE)


if __name__ == "__main__":
    main()
