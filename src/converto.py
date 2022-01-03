import numpy as np


class ImageEncoder:
    def __init__(self, fringe: int = 10):
        '''
        Initialized the ImageaEncoder Class

        Parameters
        ----------
        fringe: int, represents the range of pixels that will
            be considered alike.
        '''
        self.map = self.__genMap(fringe=fringe)

    def convertImage(self, img: np.array, out_filename: str = 'img_enc_gen.txt'):
        '''
        Converts the image into an ASCII representation

        Parameters:
        -----------
        img : np.array represents the input image
        out_filename: str, represents the filename output
        '''
        # make sure that img is 2d array
        assert(len(img.shape) == 2)

        h, w = img.shape

        with open(out_filename, mode='w+') as f:
            for y in range(h):
                for x in range(w):
                    val = int(img[y, x])
                    f.write(self.map[val])
                    f.write(f'{chr(32)+chr(32)}')
                f.write('\n')

        print("Successful")

    def __genMap(self, fringe: int, start_ASCII=33) -> list:
        '''
        Generates a random table for the image to encode
        using ASCII Characters

        Parameters
        ----------
        fringe : int
            represents the sequence of characters that will be treated
            the same
        start_ascii: int Default=33 (empirical choice)
            represents the starting ASCII code to be used

        Returns
        -------
        map : List
            map of ASCII Encodings
        '''
        # generate characters for every fringe
        MAX_IMG_VALUE = 255
        n_chars = MAX_IMG_VALUE//fringe
        ASCII_map = []

        for i in range(0, MAX_IMG_VALUE+1):
            ASCII_map.append(chr(start_ASCII))

            # if the fringe size is met then change the ASCII value
            if not i % fringe:
                start_ASCII += 1

        # return the map (Note that this is irreversible operation)
        return ASCII_map
