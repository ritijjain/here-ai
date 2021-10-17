import sys
import cv2
import face_recognition
import pickle

def register_face(pickle_file_name):
    
    # Load the known faces embeddings if they exits
    try:
        f=open(pickle_file_name,'rb')
        embed_dictt=pickle.load(f)
        f.close()
    except:
        embed_dictt={}

    while True:

        ref_id=input('Enter your unique ID (or "q" to quit): ')

        if ref_id=='q':
            break

        print('''
        Once you see the viewfinder, align your face with the frame.
        
        Press 's' to take a picture. You must take 3 pictures of your face, ideally at different angles. 
        ''')


        for i in range(3):
            key = cv2.waitKey(1)
            webcam = cv2.VideoCapture(0)
            while True:
            
                check, frame = webcam.read()

                cv2.imshow('Capturing', frame)
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1]
        
                key = cv2.waitKey(1)

                if key == ord('s') : 
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    if face_locations != []:
                        face_encoding = face_recognition.face_encodings(frame)[0]
                        if ref_id in embed_dictt:
                            embed_dictt[ref_id]+=[face_encoding]
                        else:
                            embed_dictt[ref_id]=[face_encoding]
                    
                    webcam.release()
                    cv2.destroyAllWindows()  
                    cv2.waitKey(1)   
                    print(f'Face registered successfully for {ref_id}.')
                    print('You may register additional faces or quit by entering q.')
                    break
                elif key == ord('q'):
                    print('Aborted. Face not registered.')
                    webcam.release()
                    cv2.destroyAllWindows()
                    cv2.waitKey(1)
                    break        
    f=open(pickle_file_name,'wb')
    pickle.dump(embed_dictt,f)
    print(embed_dictt)
    f.close()
    print(f'Successfully quit. Your file {pickle_file_name} now has {len(embed_dictt)} faces total.')