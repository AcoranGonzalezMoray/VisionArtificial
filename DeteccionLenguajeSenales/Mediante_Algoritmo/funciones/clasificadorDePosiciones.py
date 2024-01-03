import cv2

def clasificadorDePosiciones(dedos, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    detected_letter = None

    if dedos == [1, 1, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'A', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("A")
        detected_letter = 'A'

    if dedos == [0, 0, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'B', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("B")
        detected_letter = 'B'

    if dedos == [1,1,1,1,1,1]:  #[1,0,1,0,0,0]
        cv2.rectangle(frame,(0,0),(100,100),(255,255,255), -1)
        cv2.putText(frame,'C',(20,80),font,3,(0,0,0),2,cv2.LINE_AA)
        print("C")
        detected_letter = 'C'

    if dedos == [0, 0, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'D', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("D")
        detected_letter = 'D'

    if dedos == [0, 0, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'E', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("E")
        detected_letter = 'E'

    if dedos == [1, 1, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'F', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("F")
        detected_letter = 'F'

    # falla
    if dedos == [1, 1, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'G', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("G")
        detected_letter = 'G'

    if dedos == [1, 0, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'H', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("H")
        detected_letter = 'H'

    if dedos == [0, 0, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'I', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("I")
        detected_letter = 'I'

    if dedos == [0, 0, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("J")
        detected_letter = 'J'

    if dedos == [1, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'K', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("K")
        detected_letter = 'K'

    if dedos == [1, 1, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'L', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("L")
        detected_letter = 'L'

    #falla
    if dedos == [1, 1, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'M', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("M")
        detected_letter = 'M'

    #falla
    if dedos == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'N', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("N")
        detected_letter = 'N'

    if dedos == [1, 0, 1, 0, 0, 1]:  # [1, 0, 1, 0, 0, 0]
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'O', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("O")
        detected_letter = 'O'

    #Falla
    if dedos == [0, 1, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'P', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("P")
        detected_letter = 'P'

    if dedos == [1, 1, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Q', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("Q")
        detected_letter = 'Q'

    if dedos == [1, 0, 1, 1, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'R', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("R")
        detected_letter = 'R'

    if dedos == [0, 1, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'S', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("S")
        detected_letter = 'S'

    if dedos == [0, 0, 1, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'T', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("T")
        detected_letter = 'T'

    if dedos == [0, 0, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'U', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("U")
        detected_letter = 'U'

    if dedos == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
        cv2.putText(frame, 'V', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
        print("V")
        detected_letter = 'V'

    if dedos == [0, 1, 0, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'W', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("W")
        detected_letter = 'W'

    if dedos == [1, 1, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Y', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("Y")
        detected_letter = 'Y'

    return dedos, detected_letter