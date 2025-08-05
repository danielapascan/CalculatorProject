import os

class Settings:
    USERNAME: str = os.getenv("MATHOPS_USERNAME", "admin")
    PASSWORD: str = os.getenv("MATHOPS_PASSWORD", "secret")
    ENABLE_CACHE: bool = os.getenv("MATHOPS_ENABLE_CACHE", "true").lower() == "true"

settings = Settings()
