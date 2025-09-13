from pydantic import BaseModel, Field
from typing import Optional

class Diet(BaseModel):
    favorite_food: str = Field(description="The person's favorite food.")
    
    meals_per_day: int = Field(description="The number of meals consumed per day.")
    
    is_vegetarian: bool = Field(description="Indicates if the person is a vegetarian.")
    
    average_daily_calories: int = Field(description="The average daily calorie intake.")
    
    most_common_dining_place: str = Field(description="The most common place for dining (e.g., home, office, restaurant).")
    
    meat_percentage: float = Field(description="The percentage of meat in the diet (a value from 0 to 100).")
    
    # Pydantic v2 style for a complete example
    model_config = {
        "json_schema_extra": {
            "example": {
                "favorite_food": "Pizza",
                "meals_per_day": 3,
                "is_vegetarian": False,
                "average_daily_calories": 2200,
                "most_common_dining_place": "Home",
                "meat_percentage": 30.5
            }
        }
    }