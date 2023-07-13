from typing import List
from typing import Optional

from fastapi import Request


class DepositForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.hash: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.hash = form.get("hash")

    async def is_valid(self):
        if not self.hash:
            self.errors.append("ошибка")
        if not self.errors:
            return True
        return False