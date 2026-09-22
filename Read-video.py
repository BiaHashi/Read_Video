import cv2

vid = cv2.VideoCapture(0)

if vid.isOpened() == False:
    print("Não foi possível ler o feed da câmera")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

