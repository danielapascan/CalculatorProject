from fastapi import APIRouter
from app.models import FibonacciRequest, OperationResponse
from app.service import calculate_fibonacci
from app.db import save_operation
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/fibonacci", response_model=OperationResponse)
def fibonacci_op(req: FibonacciRequest):
    logger.info(f"Received fibonacci request: n={req.n}")
    result = calculate_fibonacci(req.n)
    logger.info(f"Calculated fibonacci({req.n}) = {result}")
    save_operation("fibonacci", f"n={req.n}", result)
    logger.info("Fibonacci operation saved to DB.")
    return {"result": result}
