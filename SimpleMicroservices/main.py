from __future__ import annotations

import os
import socket
from datetime import datetime, date
from typing import Dict, List, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, Query, Path

from models.diet import Diet

from models.menu import Menu

port = int(os.environ.get("FASTAPIPORT", 8000))

# -----------------------------------------------------------------------------
# Fake in-memory "databases"
# -----------------------------------------------------------------------------
diets: Dict[UUID, Diet] = {}
menus: Dict[UUID, Menu] = {}

app = FastAPI(
    title="Diet & Menu API",
    description="A simple API for managing Diet and Menu records.",
    version="0.1.0",
)

# -----------------------------------------------------------------------------
# Diet endpoints
# -----------------------------------------------------------------------------
@app.post("/diets", response_model=Diet, status_code=201)
def create_diet(diet: Diet):
    diet_id = uuid4()
    diets[diet_id] = diet
    return diet

@app.get("/diets", response_model=List[Diet])
def list_diets():
    return list(diets.values())

# -----------------------------------------------------------------------------
# Menu endpoints (using all 4 REST methods)
# -----------------------------------------------------------------------------
@app.post("/menus", response_model=Menu, status_code=201)
def create_menu(menu: Menu):
    if menu.id in menus:
        raise HTTPException(status_code=400, detail="Menu with this ID already exists")
    menus[menu.id] = menu
    return menu

@app.get("/menus", response_model=List[Menu])
def list_menus():
    return list(menus.values())

@app.get("/menus/{menu_id}", response_model=Menu)
def get_menu(menu_id: UUID):
    if menu_id not in menus:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menus[menu_id]

@app.put("/menus/{menu_id}", response_model=Menu)
def update_menu(menu_id: UUID, menu: Menu):
    if menu_id not in menus:
        raise HTTPException(status_code=404, detail="Menu not found")
    if menu.id != menu_id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    menus[menu_id] = menu
    return menus[menu_id]

@app.delete("/menus/{menu_id}", status_code=204)
def delete_menu(menu_id: UUID):
    if menu_id not in menus:
        raise HTTPException(status_code=404, detail="Menu not found")
    del menus[menu_id]
    return None

# -----------------------------------------------------------------------------
# Root
# -----------------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to the Diet & Menu API. See /docs for OpenAPI UI."}

# -----------------------------------------------------------------------------
# Entrypoint for `python main.py`
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)