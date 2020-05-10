import cv2
import numpy as np


IMAGE_LABEL = "STREAM"
HSV_LABEL = "HSV COLOR VIEW"
MASK_LABEL = 'MASK'
RESULT_LABEL = 'RESULT'
HORIZONTAL_STACK_LABEL = 'HORIZONTAL_STACK'

FRAME_WIDTH = 500
FRAME_HEIGHT = 500

NAMED_WINDOW_WIDTH = 600
NAMED_WINDOW_HEIGHT = 240

NAMED_WINDOW = 'HSV'

HUE_LABELS = ['HUE MIN', 'HUE MAX', 'SAT MIN', 'SAT MAX', 'VALUE MIN', 'VALUE MAX']

VIDEO_SOURCE = 1

def empty_function(a):
    pass


def detect_colors():
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)

    cv2.namedWindow(NAMED_WINDOW)
    cv2.resizeWindow(NAMED_WINDOW, NAMED_WINDOW_WIDTH, NAMED_WINDOW_HEIGHT)

    cv2.createTrackbar('HUE MIN', NAMED_WINDOW, 0, 179, empty_function)
    cv2.createTrackbar('HUE MAX', NAMED_WINDOW, 179, 179, empty_function)
    cv2.createTrackbar('SAT MIN', NAMED_WINDOW, 0, 255, empty_function)
    cv2.createTrackbar('SAT MAX', NAMED_WINDOW, 255, 255, empty_function)
    cv2.createTrackbar('VALUE MIN', NAMED_WINDOW, 0, 255, empty_function)
    cv2.createTrackbar('VALUE MAX', NAMED_WINDOW, 255, 255, empty_function)

    while True:
        _, img = cap.read()
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos('HUE MIN', NAMED_WINDOW)
        h_max = cv2.getTrackbarPos('HUE MAX', NAMED_WINDOW)
        s_min = cv2.getTrackbarPos('SAT MIN', NAMED_WINDOW)
        s_max = cv2.getTrackbarPos('SAT MAX', NAMED_WINDOW)
        v_min = cv2.getTrackbarPos('VALUE MIN', NAMED_WINDOW)
        v_max = cv2.getTrackbarPos('VALUE MAX', NAMED_WINDOW)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        mask = cv2.inRange(img_hsv, lower, upper)

        result = cv2.bitwise_and(img, img, mask=mask)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        horizon_stack = np.hstack([img, mask, result])


        cv2.imshow(HORIZONTAL_STACK_LABEL, horizon_stack)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



