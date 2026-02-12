from pydantic import BaseModel


class FieldProperties(BaseModel):
    required: bool = False
    type: str = "string"