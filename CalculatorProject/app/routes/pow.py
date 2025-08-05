from fastapi import APIRouter
from app.models import PowRequest, OperationResponse
from app.service import calculate_pow
from app.db import save_operation
import logging


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/pow", response_model=OperationResponse)
def pow_op(req: PowRequest):
    logger.info(f"Received pow request: x={req.x}, y={req.y}")
    result = calculate_pow(req.x, req.y)
    logger.info(f"Result: {result}")
    save_operation("pow", f"x={req.x},y={req.y}", result)
    return {"result": result}