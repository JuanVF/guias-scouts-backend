from pydantic import BaseModel, validator


class LoginBody(BaseModel):
    email: str
    password: str

    @validator('email')
    def email_must_be_valid(cls, v):
        # Simple example of custom email validation logic
        if "@" not in v or "." not in v:
            raise ValueError('Invalid email address')
        # Add any custom validation logic here
        return v
