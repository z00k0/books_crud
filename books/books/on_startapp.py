from django.contrib.auth import get_user_model

from books.settings import env

User = get_user_model()

with env.prefixed(f"SUPERUSER_"):
    username = env.str("USERNAME")
    password = env.str("PASSWORD")

    # Base user
    user_instance = User.objects.filter(username=username).first()
    if not user_instance:
        User.objects.create_superuser(username=username, password=password)
