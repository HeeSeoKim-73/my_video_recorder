import cv2 as cv
print(cv.__version__)

video_file="rtsp://210.99.70.120:1935/live/cctv001.stream"
video=cv.VideoCapture(video_file)

target=cv.VideoWriter()
target_file="record.avi"
fourcc=cv.VideoWriter_fourcc(*'XVID')

record=False
flip=False

if video.isOpened():
    fps=video.get(cv.CAP_PROP_FPS)
    if fps==0:
        fps=30

    while True:
        valid,img=video.read()

        if not valid:
            break
        

        if not target.isOpened():
            h,w,*_=img.shape
            is_color=(img.ndim>2) and (img.shape[2]>1)
            target.open(target_file,fourcc,fps,(w,h),is_color)

        if record:
            cv.circle(img,(30,30),10,(0,0,255),-1)
            target.write(img)

        if flip:
            img=cv.flip(img,1)

        cv.imshow("Video Player",img)

        key=cv.waitKey(1)

        if key==27:
            break

        if key==32:
            record=not record

        if key==ord('f'):
            flip=not flip
        
    video.release()
    target.release()
    cv.destroyAllWindows()
