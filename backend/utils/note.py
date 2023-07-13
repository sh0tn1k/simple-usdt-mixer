import secrets

def note_generate(amount:str):
  secret_key = secrets.token_hex(70)
  note = "sqb_"+"trx"+"_"+str(amount)+"_0x"+secret_key
  return note

print(note_generate("1"))