#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from abc import ABC, abstractmethod
from ingenico.direct.sdk.call_context import CallContext
from ingenico.direct.sdk.domain.session_request import SessionRequest
from ingenico.direct.sdk.domain.session_response import SessionResponse


class ISessionsClient(ABC):
    """
    Sessions client interface. Thread-safe.
    """

    @abstractmethod
    def create_session(self, body: SessionRequest, context: CallContext = None) -> SessionResponse:
        """
        Resource /v2/{merchantId}/sessions - Create session

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CreateSessionApi

        :param body: :class:`ingenico.direct.sdk.domain.session_request.SessionRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.session_response.SessionResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
