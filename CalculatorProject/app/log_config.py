import os
import logging

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", "app.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
