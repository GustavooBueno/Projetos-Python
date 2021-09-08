import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow('Video da Webcam', frame)
        key = cv2.waitKey(5)
        if key == 27: # tecla 27 é o ESC
            break
    cv2.imwrite('Foto.png', frame)

webcam.release()
cv2.destroyAllWindows()