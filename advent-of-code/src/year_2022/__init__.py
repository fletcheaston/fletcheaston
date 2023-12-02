from fastapi import APIRouter

from . import day_1, day_2, day_3, day_4

router = APIRouter()

router.include_router(day_1.router, prefix="/day-1")
router.include_router(day_2.router, prefix="/day-2")
router.include_router(day_3.router, prefix="/day-3")
router.include_router(day_4.router, prefix="/day-4")