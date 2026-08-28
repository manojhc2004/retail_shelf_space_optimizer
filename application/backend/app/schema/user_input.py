from fastapi import Form
from pydantic import BaseModel

class UserInput(BaseModel):
    min_support: float
    greater_than: float
    threshold: float
    shelf_capacity: int

    @classmethod
    def as_form(
        cls,
        min_support: float = Form(...),
        greater_than: float = Form(...),
        threshold: float = Form(...),
        shelf_capacity: int = Form(...)
    ):
        return cls(
            min_support=min_support,
            greater_than=greater_than,
            threshold=threshold,
            shelf_capacity=shelf_capacity
        )