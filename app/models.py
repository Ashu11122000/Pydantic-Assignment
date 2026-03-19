from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    id: int
    name: str
    age: int = 18
    email: EmailStr
    is_active: bool = True

    @field_validator("age")
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age must be positive")
        if value > 120:
            raise ValueError("Age too large")
        return value

    @field_validator("name")
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value