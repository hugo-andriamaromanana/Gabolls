from pydantic import BaseModel as __BaseModel


class BaseModel(__BaseModel):
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
