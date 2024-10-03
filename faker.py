from faker import Faker

fake = Faker()

print("Fake Data:")
for _ in range(10):
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    print(f"Name: {name}, Email: {email}, Phone Number: {phone_number}")