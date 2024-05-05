from fastapi import FastAPI, Response, HTTPException, Depends, APIRouter

from .. import schemas

import stripe

router = APIRouter(prefix="/checkout", tags=["Post"])

stripe.api_key = "sk_test_51PCw7l04ic3oUtoNIIC1RKxAdqR7jM1mVUGPMBGGOwSuM2xfNYsJmciLUtPMMSntJff1lSzzAwz9tODR8qqjlmPb00SiAAKYQP"


@router.get("/create-checkout-session")
def get_checkout_session():
    return {"message": "success!!"}


@router.post("/create-checkout-session")
def create_checkout_session(item: schemas.CheckoutItem):
    try:
        # Create a Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.title,
                            "images": [item.image_url],
                        },
                        "unit_amount": item.price,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="https://www.google.com?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="https://www.google.com/cancel",
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
