from typing import List
from typing import Optional

from fastapi import Request


class WithdrawForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.note: Optional[str] = None
        self.address: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.note = form.get("note")
        self.address = form.get("address")

    async def is_valid(self):
        if not self.note:
            self.errors.append("ошибка")
        if not self.errors:
            return True
        return False