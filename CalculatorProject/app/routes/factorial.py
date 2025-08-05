import logging
from fastapi import APIRouter
from app.models import FactorialRequest, OperationResponse
from app.service import calculate_factorial
from app.db import save_operation

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/factorial", response_model=OperationResponse)
def factorial_op(req: FactorialRequest):
    logger.info(f"Received factorial request: n={req.n}")
    result = calculate_factorial(req.n)
    logger.info(f"Calculated factorial({req.n}) = {result}")
    save_operation("factorial", f"n={req.n}", result)
    logger.info("Factorial operation saved to DB.")
    return {"result": result}
