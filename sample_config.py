HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID", "17221046"])
    API_HASH = environ["API_HASH", "233ef51a2c05a3979f95d7c7730cf320"]
    SESSION_STRING = environ[
        "BQBa1twSr7GwBqVgA2cdxK4xnt8zTSoYuPvmch0HQ-KgmEbn238U6Dhv0XDubJU5YSbL9FcDRRE10J3ivyD6NBUHlIZQpBmOtrEY4iKD1qLcpyLzFEwRgaGD4ydKxZLDYqMyw6PQc69SvQl1HbYGH4s5qNY6Cp2b780mFaXXtD-NG-oG76ca5kh3tSAEA_3CibOKOgho0hR-D0vjOjZecMd71kVfj2-U3I9TG4vv0zwJHTdQwUtNF5I-qfuDQmsgZ81A8G5pqjEG9rD7WLzQUMOpatLbwHLPJ3_ELOo05AFpK-Mebg5xGq41ScsjI0Rp-eP_RJCBFLuvMwkh-_nCx3a-AAAAAUqDigcA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY", "OMUSBV-GTVUWO-ZBJHDN-JILMRR-ARQ"]
    CHAT_ID = int(environ["CHAT_ID", "-1001573996982"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["512"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://arq.hamker.in"
