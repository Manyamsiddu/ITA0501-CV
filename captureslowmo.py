import cv2
video_path = 'path_to_your_video.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video file")
    exit()
fps = int(cap.get(cv2.CAP_PROP_FPS))
cv2.namedWindow('Original Video', cv2.WINDOW_NORMAL)
cv2.namedWindow('Slow Motion', cv2.WINDOW_NORMAL)
cv2.namedWindow('Fast Motion', cv2.WINDOW_NORMAL)
slow_factor = 2  # Increase for slower motion
fast_factor = 2  # Decrease for faster motion
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Original Video', frame)
    if slow_factor > 1:
        for _ in range(slow_factor - 1):
            ret, _ = cap.read()
            if not ret:
                break
    if fast_factor > 1:
        for _ in range(fast_factor - 1):
            ret, _ = cap.read()
            if not ret:
                break
    if slow_factor > 1:
        cv2.imshow('Slow Motion', frame)
    if fast_factor > 1:
        cv2.imshow('Fast Motion', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
