import requests
from faker import Faker
import random
import string
import concurrent.futures

faker = Faker()

def generate_random_email():
    return faker.email()

def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def generate_random_name():
    return faker.name()

def register_user(url, payload, headers):
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Success! Registration successful.")
    else:
        print("Registration failed. Status code:", response.status_code)

url = "https://makishop.xyz/api/v2/register"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "th-TH,th;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}
referrer = "https://makishop.xyz/register"

random_username = generate_random_name().lower().replace(' ', '')  # Generate a random username from the random name
random_email = generate_random_email()
random_password = generate_random_password()

payload = {
    "username": random_username,
    "Email": random_email,
    "password": random_password
}

NUM_REQUESTS = 10

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_REQUESTS) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(register_user, url, payload, headers) for _ in range(NUM_REQUESTS)]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)
