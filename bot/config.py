import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5485848281:AAECnvCl7wOF_SpAzLE3WebAgbJXA8i7Rd4")

    SESSION_NAME = os.environ.get("SESSION_NAME", "utubeitbot")

    API_ID = int(os.environ.get("API_ID", "5615631")

    API_HASH = os.environ.get("API_HASH", "f65d600ff580456871cfddc086337b7a")

    CLIENT_ID = os.environ.get("CLIENT_ID", "921912615039-42h2eg2tsqcmbig6mae5df8vai54mbff.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "GnsnVpyT3DT9cJStuexDOJ55")

    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1496802577")

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["public"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = True

    CRED_FILE = "auth_token.txt"
