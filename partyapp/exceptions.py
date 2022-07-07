
from rest_framework.exceptions import APIException
class PoliticalPartyIdNotAvailable(APIException):
    default_detail = 'Specified political party id is not available'

class PoliticalLeaderIdNotAvailable(APIException):
    default_detail = 'Specified political leader id is not available'

class DevelopmentIdNotAvailable(APIException):
    default_detail = 'Specified development id is not available'

class InvalidData(APIException):
    default_detail = 'Specified data is invalid'

class PoliticalLeaderIdIdNotAvailable(APIException):
    default_detail = 'Specified political leader id is not available'

class PoliticalPartyIdIdNotAvailable(APIException):
    default_detail = 'Specified political party id is not available'
