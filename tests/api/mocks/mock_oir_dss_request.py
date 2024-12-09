from . import GetDssOirByIdDto


class DssOirMocks:
    OIR_ID: str = "9d158f59-80b7-4c11-9c0c-8a2b4d936b2d"

    INVALID_OIR_ID: str = "000000"

    DSS_GET_OIR_BY_ID_RESPONSE: GetDssOirByIdDto = {
        "operational_intent_reference": {
            "id": "2f8343be-6482-4d1b-a474-16847e01af1e",
            "flight_type": "VLOS",
            "manager": "uss1",
            "uss_availability": "Unknown",
            "version": 1,
            "state": "Accepted",
            "ovn": "9d158f59-80b7-4c11-9c0c-8a2b4d936b2d",
            "time_start": {"value": "2024-11-12T23:20:50.52Z", "format": "RFC3339"},
            "time_end": {"value": "2024-12-12T23:20:50.52Z", "format": "RFC3339"},
            "uss_base_url": "https://uss.example.com/utm",
            "subscription_id": "78ea3fe8-71c2-4f5c-9b44-9c02f5563c6f",
        }
    }
