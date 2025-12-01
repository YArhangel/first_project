from dotenv import load_dotenv
import os

def print_author():
    # Загружаем переменные из .env
    load_dotenv()

    # Читаем переменную AUTHOR
    author = os.getenv("AUTHOR", "Автор не указан")

    print(f"Автор проекта: {author}")


if __name__ == "__main__":
    print("Hello from repository!")
    print_author()

