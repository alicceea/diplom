import os

from dotenv import load_dotenv

load_dotenv()


class ConfigureLJ:
    username = os.getenv('lj_username')
    password = os.getenv('lj_password')
    sleep_wait_medium = 3
    sleep_wait_short = 0.3
    base_person_url = f'https://www.{username}.livejournal.com'
    login_url = 'https://www.livejournal.com/login.bml?returnto=https%3A%2F%2Fwww.livejournal.com%2F&ret=1'
