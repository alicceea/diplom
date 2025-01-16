import os

from dotenv import load_dotenv

load_dotenv()


class ConfigureLJ:
    username = os.getenv('lj_username')
    password = os.getenv('lj_password')
    base_person_url = f'https://www.{username}.livejournal.com'
    login_url = 'http://www.livejournal.com/login.bml'
    sleep_wait_medium = 3
    sleep_wait_short = 0.3

