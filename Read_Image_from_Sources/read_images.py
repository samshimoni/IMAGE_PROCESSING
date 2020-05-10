"""
this is a simple demo for reading from webcam
"""
import cv2

LENA_PATH = "../Resources/lena.png"
LENA_NAME = "Lena"
INFINITY = 0

FRAME_WIDTH_ID_NUMBER = 3
FRAME_HEIGHT_ID_NUMBER = 4

FRAME_WIDTH = 1024
FRAME_HEIGHT = 768

RES_WIDTH = 600
RES_HEIGHT = 400

DRONE_FILM = "Resources/DJI_0017.MP4"
MAIN_CAMERA = 0
SECOND_CAMERA = 0

VIDEO_FRAME_NAME = "Stream"

QUIT_BUTTON = 'q'


def show_image(img_name, img_path):
    img_from_camera = cv2.imread(img_path)
    cv2.imshow(img_name, img_from_camera)
    cv2.waitKey(INFINITY)


def show_film_or_camera(stream_path, stream_name, resolution=(RES_WIDTH, RES_HEIGHT)):
    camera_feed = True
    capture = cv2.VideoCapture(stream_path)

    if stream_path == MAIN_CAMERA or stream_path == SECOND_CAMERA:
        capture.set(FRAME_WIDTH_ID_NUMBER, FRAME_WIDTH)
        capture.set(FRAME_HEIGHT_ID_NUMBER, FRAME_HEIGHT)
    else:
        camera_feed = False

    while True:
        success, img = capture.read()

        if success is False:
            print(f"failed read from source: { stream_path }")
            break

        if camera_feed is False:
            img = cv2.resize(img, resolution)

        cv2.imshow(stream_name, img)

        if cv2.waitKey(1) & 0xFF == ord(QUIT_BUTTON):
            break


def main():
    #show_image(LENA_NAME, LENA_PATH)
    show_film_or_camera(MAIN_CAMERA, VIDEO_FRAME_NAME)


if __name__ == "__main__":
    main()

