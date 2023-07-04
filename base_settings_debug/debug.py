from decimal import Decimal

from moneyed import Money
from pydantic import BaseModel, BaseSettings


class TaxData(BaseSettings):
    federal_taxes: str = "finex_engine/wing_planner/tax/data/federal.taxes.json"
    fica_taxes: str = "finex_engine/wing_planner/tax/data/fica.taxes.json"


class IncomeTaxData(BaseModel):
    federal_income_tax: Money
    effective_federal_income_tax_rate: Decimal
    state_income_tax: Money
    effective_state_income_tax_rate: Decimal
    fica_tax: Money
    effective_fica_tax_rate: Decimal
    total_tax: Money
    effective_total_tax_rate: Decimal

    class Config:
        arbitrary_types_allowed = True
