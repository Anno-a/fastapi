from decimal import Decimal
from pydantic import BaseModel, Field
from ch04.models import SexValue

class EmpCreate(BaseModel):
    id: int = Field(description='员工id')
    sal: Decimal = Field(description='员工id')
    name: str = Field(description='员工name')
    gender: SexValue = Field(description='员工id')
    bonus: Decimal | None = Field(default=None)

    class Config:
        from_attributes = True