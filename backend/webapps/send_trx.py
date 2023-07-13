from fastapi import Request
from tronpy import Tron
from tronpy.keys import PrivateKey
from core.config import Settings

client = Tron(network='shasta')
result_send = None

def send_trx(to_address:str, amount:float):
  priv_key = PrivateKey(bytes.fromhex(Settings.TRON_ADDRESS_PRIV_KEY))# Private key от ключа с которго отправля
  txn = (
    client.trx.transfer(Settings.TRON_ADDRESS, to_address, int(amount - 1_000_000))
    .memo("s")
    .build()
    .inspect()
    .sign(priv_key)
    .broadcast()
  )
  
  if txn['result'] == True:
    result_send = "Возврат успешно отправлен"
    return result_send
  else:
    result_send = "Возврат не отправлен"
    return result_send
  
def send_commision_trx(owner_address: str, private_key:str, amount_user: int):
  priv_key = PrivateKey(bytes.fromhex(private_key))# Private key от ключа с которго отправляют
  commision = float(amount_user) * Settings.COMMISSION
  txn = (
    client.trx.transfer(owner_address, Settings.TRON_ADDRESS, int(commision) * 1_000_000)
    .memo("коммисия площадки")
    .build()
    .inspect()
    .sign(priv_key)
    .broadcast()
  )
  if txn['result'] == True:
    return commision
  else:
    return False