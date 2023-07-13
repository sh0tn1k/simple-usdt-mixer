from fastapi import Depends
import requests
import datetime as dt
from core.config import Settings
from db.repository.transaction import get_transaction
from db.session import get_db
from db.repository.transaction import create_new_transaction
from tronpy.tron import Tron

tron = Tron(network="shasta")

def tron_get_transactions(note:str,db: requests.Session = Depends(get_db)):
  url = "https://api.shasta.trongrid.io/v1/accounts/" + Settings.TRON_ADDRESS + "/transactions"
  with open("last_ts.txt","r") as file:
    last_txid = file.read()
  response = requests.get(
    url,
    params={
      'limit': 200, #200 max
      'only_to': True,
      #'only_confirmed': True,
      'min_timestamp': str(last_txid)
    },
    headers={"accept": "application/json"})
  if response.json().get('data', []) == []:
    return False
  else:
    for transaction in response.json().get('data', []):
      amount = float(transaction.get('raw_data', {}).get('contract', [{}])[0].get('parameter', {}).get('value', {}).get('amount')) # / 1_000_000
      txID = transaction.get('txID', '')
      time = dt.datetime.fromtimestamp(float(transaction.get('block_timestamp', '')) / 1000)
      if get_transaction(hash=txID, db=db) == None:
        create_new_transaction(db=db, txid=txID, amount=amount, date=time, status="СОЗДАН", note=note)
        with open("last_ts.txt", mode="w") as file1:
          file1.write(str(transaction.get('block_timestamp', '')))
          file1.close()
        return True