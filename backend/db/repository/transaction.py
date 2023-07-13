from sqlalchemy.orm import Session
from datetime import datetime
from db.models.transactions import Transaction

def create_new_transaction(db:Session, txid:str, amount:int, date:datetime, status:str, note:str):
    transaction = Transaction(
        txid=txid,
        amount=amount,
        date=date,
        status = status,
        note = note
        )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_transaction(hash:str,db: Session):
    transaction = db.query(Transaction).filter(Transaction.txid == hash).first()
    return transaction

def get_transaction_by_id(id:int,db: Session):
    transaction = db.query(Transaction).filter(Transaction.id == id).first()
    return transaction

def check_note(note:str,db: Session):
    transaction = db.query(Transaction).filter(Transaction.note == note).first()
    return transaction

def update_transaction(id:int,db: Session):
    transaction = db.query(Transaction).filter(Transaction.id == id).first()
    if transaction:
        transaction.status = "ЗАВЕРШЕНО"
        transaction.note = "обнулена"
    db.commit()

def count_of_transaction(db: Session):
    transaction = db.query(Transaction).count()
    return transaction

def get_transactions(db: Session):
    transaction = db.query(Transaction).order_by(Transaction.id.desc())[:10]
    return transaction