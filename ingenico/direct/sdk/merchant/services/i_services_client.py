#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from abc import ABC, abstractmethod
from ingenico.direct.sdk.call_context import CallContext
from ingenico.direct.sdk.domain.get_iin_details_request import GetIINDetailsRequest
from ingenico.direct.sdk.domain.get_iin_details_response import GetIINDetailsResponse
from ingenico.direct.sdk.domain.test_connection import TestConnection


class IServicesClient(ABC):
    """
    Services client interface. Thread-safe.
    """

    @abstractmethod
    def test_connection(self, context: CallContext = None) -> TestConnection:
        """
        Resource /v2/{merchantId}/services/testconnection - Test connection

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/TestConnectionApi

        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.test_connection.TestConnection`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """

    @abstractmethod
    def get_iin_details(self, body: GetIINDetailsRequest, context: CallContext = None) -> GetIINDetailsResponse:
        """
        Resource /v2/{merchantId}/services/getIINdetails - Get IIN details

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetIINDetailsApi

        :param body: :class:`ingenico.direct.sdk.domain.get_iin_details_request.GetIINDetailsRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.get_iin_details_response.GetIINDetailsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
