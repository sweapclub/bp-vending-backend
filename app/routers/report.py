from fastapi import APIRouter
from app.dao.dao_report import generate_report
from app.dto.dto_report import OutputReport, Report
router = APIRouter(
    prefix="/report",
    tags=["Report"],
    responses={404: {"description": "Not found"}}
)


@router.get('/', summary="Get all report", response_model=OutputReport)
async def get_report():
    list_report, error_message = generate_report()
    if error_message != None:
        return OutputReport(status="Fail", errorMessage=error_message)

    result = []
    for r in list_report:
        result.append(Report(
            reportTs=r.report_ts,
            productName=r.product_name,
            productPrice = r.product_price,
            amount=r.amount,
            takeMoney=r.input_money,
            change=r.change
        ))
    return OutputReport(status="Success", data=result)
