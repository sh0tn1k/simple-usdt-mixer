from fastapi import APIRouter, Depends, status
from fastapi import Request
from sqlalchemy.orm import Session
from webapps.forms.forms_withdraw import WithdrawForm
from db.repository.transaction import count_of_transaction, get_transactions, check_note, update_transaction, get_transaction_by_id
from core.get_transaction import tron_get_transactions
from webapps.forms.forms_deposit import DepositForm
from utils.note import note_generate
from webapps.send_trx import send_trx
from db.session import get_db
from fastapi.templating import Jinja2Templates
from fastapi import responses


templates = Jinja2Templates(directory="templates")
router = APIRouter()

# Отображение главной страницы
@router.get("/")
async def main(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        "general_pages/main.html",
        {
            "request": request,
            "deposit_count": count_of_transaction(db=db),
            "transactions": get_transactions(db=db),
            "info": ""
        }
    )

@router.post("/")
async def main(request: Request, db: Session = Depends(get_db)):
    note = note_generate(amount=100)
    return templates.TemplateResponse(
        "general_pages/main.html",
        {
            "request": request,
            "note": note,
            "deposit_count": count_of_transaction(db=db),
            "transactions": get_transactions(db=db),
            "info": ""
        }
    )

@router.post("/send")
async def main(request: Request, db: Session = Depends(get_db)):
    form = DepositForm(request)
    await form.load_data()
    if await form.is_valid():
      tron_get_transactions(db=db, note=form.hash)
      return responses.RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    else:
       return templates.TemplateResponse("general_pages/main.html",{
          "request": request,
          "deposit_count": count_of_transaction(db=db),
          "transactions": get_transactions(db=db),
          "errors":form.__dict__["errors"],
          "info": ""
          })

@router.post("/withdraw")
async def main(request: Request, db: Session = Depends(get_db)):
    form = WithdrawForm(request)
    await form.load_data()
    if await form.is_valid():
      check = check_note(db=db, note=form.note)
      if check:
         r = send_trx(to_address=form.address, amount=check.amount)
         if r == "Возврат успешно отправлен":
            update_transaction(db=db, id=check.id)
            return templates.TemplateResponse(
               "general_pages/main.html",
               {
                  "request": request,
                  "deposit_count": count_of_transaction(db=db),
                  "transactions": get_transactions(db=db),
                  "info": check
               })
    else:
       return templates.TemplateResponse("general_pages/main.html",{
          "request": request,
          "deposit_count": count_of_transaction(db=db),
          "transactions": get_transactions(db=db),
          "errors":form.__dict__["errors"],
          "info": ""
          })