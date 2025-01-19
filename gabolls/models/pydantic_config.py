from pydantic import BaseModel as __BaseModel


class BaseModel(__BaseModel):
    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
