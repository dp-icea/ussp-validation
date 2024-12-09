# Authentication endpoint path
GET_TOKEN_PATH: str = "/token"

# Parameter name for token request

QUERY_PARAM_SUB_NAME: str = "sub"
QUERY_PARAM_SCOPE_NAME: str = "scope"
QUERY_PARAM_INTENDED_AUDIENCE_NAME: str = "intended_audience"
QUERY_PARAM_API_KEY_NAME = "apikey"

# Parameter value for token request
QUERY_PARAM_SUB_VALUE: str = "icea"
CONSTRAINT_MANAGEMENT_SCOPE_VALUE: str = "utm.constraint_management"
STRATEGIC_COORDINATION_SCOPE_VALUE: str = "utm.strategic_coordination"
INVALID_SCOPE_VALUE: str = "utm.invalid_scope"

INTENDED_AUDIENCE_DSS_VALUE: str = "core-service"
INTENDED_AUDIENCE_USSP_VALUE: str = "icea"

# Client type value
DSS_CLIENT_TYPE: str = "dss"
USSP_CLIENT_TYPE: str = "ussp"
