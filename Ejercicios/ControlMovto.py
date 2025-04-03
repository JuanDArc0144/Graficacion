import numpy as np 
import cv2 as cv
cap = cv.VideoCapture(0)
lkparm =dict(winSize=(100,100), maxLevel=2,
             criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)) 
_, vframe = cap.read()
ball_pos = np.array([[250, 250]], dtype=np.float32)
ball_pos = ball_pos[:, np.newaxis, :]
ball_pox_aux = np.array([[250, 250]], dtype=np.float32)
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
p0 = np.array([(300,300), (350,300),
               (300,350), (350,350)])
p0 = np.float32(p0[:, np.newaxis, :])
mask = np.zeros_like(vframe) 
while True:
    _, frame = cap.read()
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    new_ball_pos, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, ball_pos, None, **lk_params)
    p1, st2, err2 = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm) 
    # if new_ball_pos is not None:
    #         ball_pos = new_ball_pos
    #         a, b = ball_pos.ravel()
    #         frame = cv.circle(frame, (int(a), int(b)), 20, (0, 0, 255), -1)
    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st2 ==1]
        bp0 = p0[st2 ==1]
        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())
            dist = np.linalg.norm(nv.ravel() - vj.ravel())
            #print(i, dist)
            #frame = cv.line(frame, (c,d), (a,b), (0,0,255), 2)
            frame = cv.line(frame, (300,300), (a,b), (255,0,0), 1)
            frame = cv.line(frame, (300,350), (a,b), (255,0,0), 1)
            frame = cv.line(frame, (300,300), (350,350), (255,0,0), 1)
            frame = cv.line(frame, (300,350), (350,350), (255,0,0), 1)
            frame = cv.circle(frame, (c,d), 2, (255,0,0),-1) #AZUL
            frame = cv.circle(frame, (a,b), 5, (0,255,0),-1) #VERDE
        cv.imshow('ventana', frame)
        vgris = fgris.copy()
        if(cv.waitKey(1) & 0xff) == 27:
            break
cap.release()
cv.destroyAllWindows()