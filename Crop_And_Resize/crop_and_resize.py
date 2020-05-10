import cv2


def size_of_image(image):
    return image.shape


def resize_image(image, width, height):
    return cv2.resize(image, (width, height))


def crop_image(image, start_x, end_x, start_y, end_y):
    image_width, image_height, dim = image.shape
    if (start_x >= 0) and (start_x <= image_width) and (end_x >= 0) and (end_x <= image_width) and (start_y >= 0) and\
            (start_y <= image_height) and (end_y >= 0) and (end_y <= image_height)\
            and (start_x <= end_x) and (start_y <= end_y):
        return image[start_x:end_x, start_y:end_y]