from requests import Response
from pydantic import ValidationError

from . import GetOirByIdDto


def is_ussp_get_oir_response_compliant(data: Response) -> bool:
    try:
        return True if GetOirByIdDto.model_validate(data.json()) else False
    except ValidationError as err:
        print(err.json())
        return False
