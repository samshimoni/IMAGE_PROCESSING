from Crop_And_Resize import crop_and_resize


import cv2
LENA_PATH = "../Resources/lena.png"
LENA_LABEL = "Lena"

WIDTH = 400
HEIGHT = 400
INFINITY = 0

RESIZE_LABEL = "200X200"

CROP_START_X = 10
CROP_START_Y = 20
CROP_END_X = 400
CROP_END_Y = 400
CROP_LABEL = "CROPPED"


def main():
    image = cv2.imread(LENA_PATH)
    resized_image = crop_and_resize.resize_image(image, WIDTH, HEIGHT)
    cropped_image = crop_and_resize.crop_image(image, CROP_START_X, CROP_END_X, CROP_START_Y, CROP_END_Y)
    cv2.imshow(RESIZE_LABEL, resized_image)
    cv2.imshow(RESIZE_LABEL, cropped_image)
    cv2.waitKey(INFINITY)


if __name__ == '__main__':
    main()