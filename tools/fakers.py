import random
import time
from faker import Faker

fake = Faker()


def get_random_email() -> str:
    return f"test{time.time()}@example.com"


def get_random_email_fake() -> str:
    return fake.safe_email()