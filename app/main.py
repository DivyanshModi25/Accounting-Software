from .core.config import settings


def main():
    print("Hello from accounting-software!")
    print(settings.database_url)


if __name__ == "__main__":
    main()
