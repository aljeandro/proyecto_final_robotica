import numpy as np
import cv2
import requests
import imutils


def detect_ball(
        img, threshold, dp, min_dist, param1,
        param2, min_radius, max_radius):

    img_B = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)[:, :, 2]

    _, thresholded_image = cv2.threshold(img_B, threshold, 255, cv2.THRESH_BINARY)

    preprocessed_img = cv2.medianBlur(thresholded_image, 5)

    balls = cv2.HoughCircles(preprocessed_img,
                             cv2.HOUGH_GRADIENT,
                             dp,
                             min_dist,
                             param1=param1,
                             param2=param2,
                             minRadius=min_radius,
                             maxRadius=max_radius)

    if balls is not None:
        balls = np.uint16(np.around(balls))

        return True, balls[0, 0, 0], balls[0, 0, 1], balls[0, 0, 2]

    else:
        return False, None, None, None


def capture_image(url, width, height):

    img_response = requests.get(url)
    img_array = np.array(bytearray(img_response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    return imutils.resize(img, width=width, height=height)


def graph_circle(img, x_center, y_center, radius):

    img = cv2.circle(img, (x_center, y_center), radius, (0, 255, 0), 2)
    img = cv2.circle(img, (x_center, y_center), 2, (255, 0, 0), 3)

    return img


