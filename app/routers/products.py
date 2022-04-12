from fastapi import APIRouter

from app.dao.dao_product import (get_all_product, update_stock)
from app.dto.dto_product import (
    Product, OutputGetProduct, InputUpdateStock, OutputStatus)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}}
)


@router.get('/', summary="Get all product", response_model=OutputGetProduct)
async def get_products():
    list_product, error_message = get_all_product()
    if error_message != None:
        return OutputGetProduct(status="Fail", errorMessage=error_message)

    result = []
    for p in list_product:
        result.append(Product(productId=p.product_id,
                      productName=p.product_name, amount=p.amount, price=p.price))
    return OutputGetProduct(status="Success", data=result)


@router.put('/{product_id}/amount', summary="Add stock for product", response_model=OutputStatus)
async def put_update_stock(input: InputUpdateStock, product_id: str):
    if (input.updateStock < 0):
        return OutputStatus(status="Fail", errorMessage="Amount can't be minus")

    error_message = update_stock(product_id, input.updateStock)
    print(error_message)
    if error_message != None:
        return OutputStatus(status="Fail", errorMessage=error_message)
    return OutputStatus(status="Success")
