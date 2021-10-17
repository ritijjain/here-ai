from register_face import register_face
from attendance_session import attendance_session
import sys

def help():
    print('''

    Run commands using
        python run.py <command name>

    Commands
        register_face <pickle_file_name>
        attendance_session <pickle_file_name>
    
    ''')

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])