
def cart_processor(request):
    cart = {
        "20":{
            "quantity":1,
            "price":10
        }

    }
    return {"cart":cart}