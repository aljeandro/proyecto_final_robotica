import cv2
from tennis_ball_detection import detect_ball, capture_image, graph_circle
import robot_controller

#  ----------------------------------------------Constantes-------------------------------------------------------------
# Parámetros de detección de circulos
THRESHOLD = 148
DP = 1
MIN_DIST = 150
PARAM1 = 10
PARAM2 = 14
MIN_RADIUS = 0
MAX_RADIUS = 150

# Constantes de conexión
URL_CAM = "http://192.168.0.100:8080/shot.jpg"
BLUETOOTH_PORT = 'COM5'

# Constantes de resolución de la cámara
CAPTURE_WIDTH = 666
CAPTURE_HEIGHT = 375

# Constante de visualizción
WINDOW_NAME = "Cámara Android"

# Constantes de control de comportamiento
STOP_RADIUS = 70
RIGHT_TURN_THRESHOLD = (2/3) * CAPTURE_WIDTH
LEFT_TURN_THRESHOLD = (1/3) * CAPTURE_WIDTH
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    car = robot_controller.Car(BLUETOOTH_PORT)

    while True:

        capture = capture_image(URL_CAM, CAPTURE_WIDTH, CAPTURE_HEIGHT)

        ball_is_detected, x_center, y_center, radius = detect_ball(capture, THRESHOLD,
                                                                   DP, MIN_DIST,
                                                                   PARAM1, PARAM2, MIN_RADIUS,
                                                                   MAX_RADIUS)

        if ball_is_detected:
            capture = graph_circle(capture, x_center, y_center, radius)

            if radius >= STOP_RADIUS:
                car.stop()
                print("detencion")
            else:
                if x_center >= RIGHT_TURN_THRESHOLD:
                    car.right_turn()
                    print('Giro a la derecha')
                elif x_center <= LEFT_TURN_THRESHOLD:
                    car.left_turn()
                    print('Giro a la izquierda')
                else:
                    car.straight_move()
                    print('Movimiento recto')
        else:
            car.stop()
            print("En espera")

        cv2.imshow(WINDOW_NAME, capture)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
