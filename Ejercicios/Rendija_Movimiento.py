import numpy as np 
import cv2 as cv
cap = cv.VideoCapture(0)
lkparm =dict(winSize=(100,100), maxLevel=2,
             criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)) 
_, vframe = cap.read()
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
p0 = np.array([(100,100), (150,100),(200,100), (250,100),(300,100), (350,100),(400,100), (450,100),(500,100),
               (100,150), (150,150),(200,150), (250,150),(300,150), (350,150),(400,150), (450,150),(500,150),
               (100,200), (150,200),(200,200), (250,200),(300,200), (350,200),(400,200), (450,200),(500,200),
               (100,250), (150,250),(200,250), (250,250),(300,250), (350,250),(400,250), (450,250),(500,250),
               (100,300), (150,300),(200,300), (250,300),(300,300), (350,300),(400,300), (450,300),(500,300),
               (100,350), (150,350),(200,350), (250,350),(300,350), (350,350),(400,350), (450,350),(500,350),
               (100,400), (150,400),(200,400), (250,400),(300,400), (350,400),(400,400), (450,400),(500,400),
               (100,450), (150,450),(200,450), (250,450),(300,450), (350,450),(400,450), (450,450),(500,450)])
p0 = np.float32(p0[:, np.newaxis, :])
mask = np.zeros_like(vframe) 
while True:
    _, frame = cap.read()
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm) 
    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st ==1]
        bp0 = p0[st ==1]
        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())
            dist = np.linalg.norm(nv.ravel() - vj.ravel())
            #print(i, dist)
            frame = cv.line(frame, (c,d), (a,b), (0,0,255), 2)
            frame = cv.circle(frame, (c,d), 2, (255,0,0),-1)
            frame = cv.circle(frame, (a,b), 3, (0,255,0),-1)
        cv.imshow('ventana', frame)
        vgris = fgris.copy()
        if(cv.waitKey(1) & 0xff) == 27:
            break
cap.release()
cv.destroyAllWindows()