from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from sweets.shop import SweetShop, InsufficientStockError
from sweets.models import Sweet
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

shop = SweetShop()

shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
shop.add_sweet(Sweet(1002, "Gajar Halwa", "VegetableBased", 30, 15))
shop.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 10, 50))


@app.get("/")
def read_sweets(request: Request, sort_by: str = None, ascending: bool = True):
    if sort_by:
        sweets = shop.sort_sweets(sort_by=sort_by, ascending=ascending)
    else:
        sweets = shop.get_all_sweets()
    return templates.TemplateResponse("index.html", {"request": request, "sweets": sweets})

@app.get("/add")
def add_sweet_form(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})


@app.post("/add")
def add_sweet(
    request: Request,
    id: int = Form(...),
    name: str = Form(...),
    category: str = Form(...),
    price: float = Form(...),
    quantity: int = Form(...)
):
    try:
        sweet = Sweet(id=id, name=name, category=category, price=price, quantity_in_stock=quantity)
        shop.add_sweet(sweet)
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("add.html", {"request": request, "error": str(e)})


@app.get("/delete/{sweet_id}")
def delete_sweet(sweet_id: int):
    try:
        shop.delete_sweet(sweet_id)
    except Exception:
        pass  # ignore errors for now
    return RedirectResponse(url="/", status_code=303)


@app.post("/purchase/{sweet_id}")
def purchase_sweet(sweet_id: int, quantity: int = Form(...)):
    try:
        shop.purchase_sweet(sweet_id, quantity)
    except InsufficientStockError as e:
        # For simplicity, ignoring error display here; you can extend
        pass
    return RedirectResponse(url="/", status_code=303)


@app.post("/restock/{sweet_id}")
def restock_sweet(sweet_id: int, quantity: int = Form(...)):
    try:
        shop.restock_sweet(sweet_id, quantity)
    except Exception:
        pass
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)