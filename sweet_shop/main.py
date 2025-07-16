from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sweets.shop import SweetShop
from sweets.models import Sweet

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)