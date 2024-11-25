from pydantic import ValidationError

from models.perpusnas import PerpusnasModel

async def validate_data(input_dict: dict) -> dict:
    try:
        model_instance = PerpusnasModel(**input_dict)
        return model_instance
    except ValidationError as e:
        return {"error": e.errors()}