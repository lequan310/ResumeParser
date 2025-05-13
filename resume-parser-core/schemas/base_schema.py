from pydantic import BaseModel


def alias_generator(field_name: str) -> str:
    """
    Convert a field name to snake_case.
    """
    return field_name.lower()


class BaseRequestModel(BaseModel):
    """
    Base class for all request models.
    """

    class Config:
        # Allow arbitrary types in the model
        arbitrary_types_allowed = True

        # Allow extra fields in the model
        extra = "forbid"

        # Use snake_case for field names in the model
        alias_generator = alias_generator


class BaseResponseModel(BaseModel):
    """
    Base class for all response models.
    """

    class Config:
        # Allow arbitrary types in the model
        arbitrary_types_allowed = True

        # Allow extra fields in the model
        extra = "forbid"

        # Use snake_case for field names in the model
        alias_generator = alias_generator
