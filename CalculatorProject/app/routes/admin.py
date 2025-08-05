from fastapi import APIRouter, Depends
from app.db import clear_operations
from app.auth import get_current_user
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.delete("/operations/clear")
def clear_ops(user: str = Depends(get_current_user)):
    logger.info(f"User '{user}' requested DB clear.")
    clear_operations()
    logger.info("DB cleared successfully.")
    return {"message": "All operations deleted."}
