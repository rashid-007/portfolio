import os
DEBUG = True
PORT = os.environ.get("PORT", 5000)
DATABASE_URL = os.environ.get("DATABASE_URL")
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")

