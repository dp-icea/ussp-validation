from datetime import datetime, timedelta
from typing import List

from . import Volume3dDto
from . import PolygonVerticesDto
from . import Volume4dDto
from . import VOLUME_CONSTANTS


class VolumeMocks:

    CURRENT_DATE: datetime = datetime.now().isoformat()

    THIRTY_DAYS_FROM_CURRENT_DATE: datetime = (
        CURRENT_DATE + timedelta(days=VOLUME_CONSTANTS.THRITY_DAYS_OFFSET)
    ).isoformat()

    POLYGON_VERTICES_COORDINATES: List[PolygonVerticesDto] = [
        {"lng": -45.56389370800656, "lat": -22.71819379959848},
        {"lng": -45.54367859425534, "lat": -22.721555860608987},
        {"lng": -45.53674640899115, "lat": -22.72240470844224},
        {"lng": -45.54187735019781, "lat": -22.708730453761277},
        {"lng": -45.56389370800656, "lat": -22.71819379959848},
    ]

    VOLUME_3D: Volume3dDto = {
        "outline_polygon": {"vertices": POLYGON_VERTICES_COORDINATES},
        "altitude_lower": {"value": 100000, "reference": "W84", "units": "M"},
        "altitude_upper": {"value": 100000, "reference": "W84", "units": "M"},
    }

    VOLUME_4D: Volume4dDto = {
        "volume": VOLUME_3D,
        "time_start": {
            "value": CURRENT_DATE,
            "format": VOLUME_CONSTANTS.DEFAULT_TIME_FORMAT,
        },
        "time_end": {
            "value": THIRTY_DAYS_FROM_CURRENT_DATE,
            "format": VOLUME_CONSTANTS.DEFAULT_TIME_FORMAT,
        },
    }
