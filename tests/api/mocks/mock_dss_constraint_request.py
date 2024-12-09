from uuid import uuid4
from faker import Faker

from . import PutConstraintRequestDto, VolumeMocks


class DssConstraintMocks:
    DSS_CONSTRAINT_ID: str = uuid4()

    DSS_OVN_CONSTRAINT_ID: str = uuid4()

    DSS_PUT_CONSTRAINT_REQUEST_BODY: PutConstraintRequestDto = {
        "extents": [VolumeMocks.VOLUME4D],
        "uss_base_url": Faker.url(),
    }
