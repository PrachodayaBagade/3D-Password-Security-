import face_recognition
import cv2

import os
from glob import glob
import mysql.connector


def face_id():
    video_capture = cv2.VideoCapture(0)

    directory = os.getcwd()
    persons = glob(directory+'/data/*')

    known_face_encodings = []
    known_face_names = []

    mySQLconnection = mysql.connector.connect(host='localhost',database='threed_password',user='root',password='')
    sql_select_Query = "select * from password3d"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    for record in records:
        print('./data/' + record[0] + '.png')
        f1_image = face_recognition.load_image_file('./data/' + record[0] + '.png')
        f1_face_encoding = face_recognition.face_encodings(f1_image)[0]
        known_face_encodings.append(f1_face_encoding)
        known_face_names.append(record[0])


    print(known_face_names)
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    name = -1
    itr = 0
    while True:

        itr += 1

        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        rgb_small_frame = small_frame[:, :, ::-1]

       
        if process_this_frame:
          
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                face_names.append(name)
               
        process_this_frame = not process_this_frame
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
          
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
           
            font = cv2.FONT_HERSHEY_DUPLEX
            if(name == 'Unknown'):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)           
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 0), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 255), 2)
            else:
                cv2.rectangle(frame, (left, top), (right, bottom), (250, 250, 250), 2)           
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (250, 250, 250), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 150, 0), 2)
     
        cv2.imshow('Video', frame)
        cv2.waitKey(1)
            
        if name != -1:
            cv2.waitKey(1000)
            break

        if itr > 150:
            break
                  
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return name    


##k = face_id()
##print(k)



