from uuid import UUID, uuid4
from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field

class Menu(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="The unique identifier for the menu.")
    menu_date: date = Field(..., description="The date of this menu.")
    cuisine: str = Field(..., description="The cuisine for today's menu (e.g., 'Sichuan', 'Cantonese').")
    dishes: List[str] = Field(..., description="A list of dishes available today.")
    has_vegetarian_option: bool = Field(..., description="Indicates if a full vegetarian option is available.")
    open_hours: str = Field(..., description="The operating hours for the canteen today.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "menu_date": "2025-09-12",
                "cuisine": "Sichuan",
                "dishes": ["Kung Pao Chicken", "Mapo Tofu"],
                "has_vegetarian_option": True,
                "open_hours": "11:00 AM - 2:00 PM"
            }
        }

    }
