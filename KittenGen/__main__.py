from app import app
from dotenv import load_dotenv
import os

load_dotenv()

ENABLE_EXTERNAL_NETWORK_ACCESS=bool(os.getenv("NETWORK_ACCESS"))

print(ENABLE_EXTERNAL_NETWORK_ACCESS)
if __name__ == '__main__':
    if ENABLE_EXTERNAL_NETWORK_ACCESS == True:
        app.run(host="0.0.0.0",port=2025)
    else:
        app.run(port=2025)
