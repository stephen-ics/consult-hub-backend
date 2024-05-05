from pydantic import BaseModel


class CheckoutItem(BaseModel):
    title: str
    image_url: str
    price: int  # Price should be in cents
