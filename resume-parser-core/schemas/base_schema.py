from pydantic import BaseModel


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
        alias_generator = lambda x: x.lower()  # Convert to snake_case


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
        alias_generator = lambda x: x.lower()  # Convert to snake_case
