from typing import Optional

class UserSchema:
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    referral_code: Optional[str] = None