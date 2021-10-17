# HereAI
A simple command line based face recognition attendance system.

![Demo Gif](demo.gif)

## Usage
Use the `python run.py register_face <pickle_file_name>` command to create or update a pickle file to store face data. Multiple pickle files can be used to manage different groups of people. Each face must be associated with a unique ID (could be anything like emails, names, student numbers as long as they are unique).

Use the `python run.py attendance_session <pickle_file_name>` to start an attendance session. Users can then walk up to the camera and be notified in the command line if they were picked up by the system. Press `q` to end the session and get a present/absent summary for the session.

## Quick Start
You can test out the scripts yourself by 
1. Downloading the files
2. Installing dependencies provided in `requirements.txt` using Pipenv or otherwise.
3. Register faces to a pickle file and then start an attendance session using the same pickle file. Refer to the [usage section](pipenv) for more details.