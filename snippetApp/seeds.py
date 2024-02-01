from faker import Faker
from django.contrib.auth.models import User
from snippetApp.models import Code
import random

fake = Faker()

def seed_db(n=10) -> None:
    try:
        # Create fake users
        # for _ in range(5):
        #     first_name = fake.first_name()
        #     last_name = fake.last_name()
        #     username = fake.user_name()
        #     email = fake.email()
        #     password = fake.password()
        #     User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # users = User.objects.all()

        # Create fake Code instances
        for _ in range(0, n):
            title = fake.sentence()
            code_content = fake.text()
            language = fake.word()
            tags = ', '.join(fake.words(random.randint(1, 5)))
            fake_user = random.choice(users)
            Code.objects.create(title=title, code_content=code_content, language=language, tags=tags, user=fake_user)

    except Exception as e:
        print(e)
