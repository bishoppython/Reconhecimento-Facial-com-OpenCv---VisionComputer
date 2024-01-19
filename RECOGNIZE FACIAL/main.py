import cv2
import mediapipe as mp

#inicializar o opencv e o mediapipe

webcam = cv2.VideoCapture(0)
solucao_recognize_face = mp.solutions.face_detection
reconhecedor_faces = solucao_recognize_face.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #Ler as Infos da WebCam
    verificador, frame = webcam.read()
    
    if not verificador:
        break
    
    #reconhecer os Rostos da imagem
    listas_rostos = reconhecedor_faces.process(frame)
    
    if listas_rostos.detections:
        for rosto in listas_rostos.detections:
                #Desenhar os rostos da imagem
            desenho.draw_detection(frame, rosto)
        
    cv2.imshow("Recognize Facial", frame)
    
    #quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27: #or ord('q') ou qualquer outra letra
        
        break
    
webcam.release()
cv2.destroyAllWindows()