import os
from dotenv import load_dotenv


def set_env():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_dir = os.path.join(base_dir, '.env')
    load_dotenv(env_dir)


set_env()