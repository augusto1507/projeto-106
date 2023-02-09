import cv2


# Crie nosso classificador de corpos


# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:

    
    
    # Leia o primeiro quadro
    ret, frame = cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("video", frame)

    # Converta cada quadro em escala de cinza
    
    # Passe o quadro para nosso classificador de corpos
    
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
