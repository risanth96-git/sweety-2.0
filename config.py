from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("29343670"))
API_HASH = getenv("6880909457:AAGIMSvHx7GZzwuf-gvVEhYgzIvpdn4Sy78")

BOT_TOKEN = getenv("6880909457:AAGIMSvHx7GZzwuf-gvVEhYgzIvpdn4Sy78", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6436690546"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("BQG_v7YAoT-VpN4uG6JQcfxIR79Ry42M6G6GlFD-B7ZkRimJG4y6OpmI8cgTxQZBRbt9l3CjJJOwXdzBcPRyWA13V4YsPXjhdrOEhPSZDpIVBjnSSSC-ymou5Qyzs_nN_3P2njRF0A2_m4c1dlKs59sNMtm-jPEe9Dd370te1yiDoKHN2vAcYizTVNwtdFLQLME_k6_UVQYxIb3E5XHN3Ncz1snvxf-b48MFKsOoN6D3X3T2Z2gVl0i4wf3IeQCgpsvqQKkn2tQ8cvIrfzM9DxWxa7yR7i8djXFamMn8IKHjN6fv1EaWA5_uI3nZ4uU9VcAMH9HKxsvn9Zm0Gf4lHAEyTsIZCAAAAAFJtncVAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/musictestttt")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/musictestttt")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7013769425").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
