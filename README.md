# here-ai
A simple command line based face recognition attendance system.

![Demo Gif](demo.gif)

Use the `python run.py register_face <pickle_file_name>` command to create or update a pickle file to store face data. Multiple pickle files can be used to manage different groups of people. 

Use the `python run.py attendance_session <pickle_file_name>` to start an attendance session. Users can then walk up to the camera and be notified in the command line if they were picked up by the system. Press `q` to end the session and get a present/absent summary for the session.