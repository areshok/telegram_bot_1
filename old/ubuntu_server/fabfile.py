
from pathlib import Path
import os

from fabric import Connection, Config


IP_SERVER = '192.168.64.9'
USERNAME_SERVER = 'ubuntu'
PASSWORD_SERVER = 'ubuntu'

USER = {'password': 'ubuntu'}

sudo_conf = Config(overrides={'sudo': {'password': 'ubuntu'}})


BASE_DIR = Path(__file__).resolve().parent.parent

serv_path = '/home/ubuntu/backend'

def create_folder_project(conn):
    result = conn.run('test -d /home/ubuntu/backend', warn=True)
    if not result.ok:
        conn.run('mkdir /home/ubuntu/backend')
        print('folder create')


def mv_project_to_server(conn):
    pass



def deploy():
    "развернуть"
    with Connection('ubuntu@192.168.64.10', connect_kwargs=USER) as conn:

        create_folder_project(conn)
        mv_project_to_server(conn)


if __name__ == '__main__':
    deploy()

    #print(BASE_DIR)


