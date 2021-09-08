#Esse é meu primeiro projeto usando a biblioteca Opencv.
#Nesse projeto através do python é possível abrir a webcam e ver em tempo real as imagens da webcam.
#Para fechar o programa basta clicar no ESC e além do programa ser fechado ele tira uma foto da última imagem que aparece na Webcam e salva como PNG.

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
