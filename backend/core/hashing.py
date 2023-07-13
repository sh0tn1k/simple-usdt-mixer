from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(plain_password):
        return pwd_context.hash(plain_password)

    @staticmethod
    def get_transaction_hash(tx_hash):
        return pwd_context.hash(tx_hash)
