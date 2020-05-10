import cv2
import numpy as np

WIDTH, HEIGHT = 350, 450
TO_POINT_LIST = [[0, 0], [WIDTH, 0], [0, HEIGHT], [WIDTH, HEIGHT]]
COLORS = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)]

ORIGIN_LABEL = "Origin Image "
OUTPUT_LABEL = "Output Image "
CLICK_COUNTER = 0
CIRCLES = np.zeros((4, 2), np.int)


def warp_image(points_list, path):
    img = cv2.imread(path)

    from_points = np.float32(points_list)
    to_points = np.float32(TO_POINT_LIST)

    matrix = cv2.getPerspectiveTransform(from_points, to_points)
    img_output = cv2.warpPerspective(img, matrix, (WIDTH, HEIGHT))

    for corner in range(0, 4):
        cv2.circle(img, (from_points[corner][0], from_points[corner][1]), 10, COLORS[corner], cv2.FILLED)

    cv2.imshow(ORIGIN_LABEL, img)
    cv2.imshow(OUTPUT_LABEL, img_output)
    cv2.waitKey(0)


def mouse_points(event, x, y, flags, params):
    global CLICK_COUNTER

    if event == cv2.EVENT_LBUTTONDOWN and CLICK_COUNTER < 4:
        CIRCLES[CLICK_COUNTER] = x, y
        CLICK_COUNTER = CLICK_COUNTER + 1
        print(CIRCLES)


def get_corners_by_clicks(img_path):
    """
     this function gets an img path wait for 4 clicks (top left top right bottom left bottom right)
     and print the output in a bird view
    """

    img = cv2.imread(img_path)

    while True:

        for corner in range(0, 4):
            cv2.circle(img, (CIRCLES[corner][0], CIRCLES[corner][1]), 3, COLORS[corner], cv2.FILLED)

        cv2.imshow(ORIGIN_LABEL, img)
        cv2.setMouseCallback(ORIGIN_LABEL, mouse_points)
        cv2.waitKey(1)

        if CLICK_COUNTER == 4:
            from_points = np.float32([CIRCLES[0], CIRCLES[1], CIRCLES[2], CIRCLES[3]])
            to_points = np.float32(TO_POINT_LIST)
            matrix = cv2.getPerspectiveTransform(from_points, to_points)
            img_output = cv2.warpPerspective(img, matrix, (WIDTH, HEIGHT))
            cv2.imshow(OUTPUT_LABEL, img_output)











