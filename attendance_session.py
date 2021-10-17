import face_recognition
import cv2
import numpy as np
import glob
import pickle

def attendance_session(pickle_file_name):
    f=open(pickle_file_name,'rb')
    embed_dictt=pickle.load(f)      
    f.close()

    known_face_encodings = []  
    known_face_ids = []  
    present = {}

    for ref_id, embed_list in embed_dictt.items():
        for my_embed in embed_list:
            known_face_encodings +=[my_embed]
            known_face_ids += [ref_id]
    
    video_capture = cv2.VideoCapture(0)

    while True:
        check, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if face_distances[best_match_index] < 0.55:
                detected_id = known_face_ids[best_match_index]
                if detected_id not in present:
                    present[detected_id] = None
                    print(f'Hello {detected_id}!')
                    
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print('Present:')
    print(", ".join(present))
    print('\n')
    print('Absent:')
    print(", ".join(list(set(known_face_ids) - set(list(present.keys())))))
    print('\n')


    