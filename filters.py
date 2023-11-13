import cv2 as cv
import numpy as np
from typing import List


def bw(im):
    return cv.cvtColor(im, cv.COLOR_BGR2GRAY)


def pixelate(im, x_size=3, y_size=20):
    h, w = im.shape[:2]
    for i in range(h):
        # copy first pixel in box
        for j in range(w):
            im[i, j] = im[i // x_size * x_size, j // y_size * y_size]
    return im


def threshold(im, filter=127):
    return np.where(im > filter, 255, 0).astype("uint8")


# [I]: im, image
# [I]: filters, list of functions and args
# [O]: image after all filters have been applied
def filter(im, filters):
    res = im
    for func, args in filters:
        res = globals()[func](res, *args)
    return res


if __name__ == "__main__":
    # Initialize the camera
    # '0' is usually the default value for the laptop's built-in camera
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # im = filter(frame, [("bw", []), ("threshold", []), ("pixelate", [])])
        im = filter(frame, [("pixelate", [])])
        cv.imshow("Frame", im)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()
