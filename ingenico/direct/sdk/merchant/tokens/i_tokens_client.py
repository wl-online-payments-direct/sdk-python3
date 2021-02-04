#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from abc import ABC, abstractmethod
from ingenico.direct.sdk.call_context import CallContext
from ingenico.direct.sdk.domain.create_token_request import CreateTokenRequest
from ingenico.direct.sdk.domain.created_token_response import CreatedTokenResponse
from ingenico.direct.sdk.domain.token_response import TokenResponse


class ITokensClient(ABC):
    """
    Tokens client interface. Thread-safe.
    """

    @abstractmethod
    def create_token(self, body: CreateTokenRequest, context: CallContext = None) -> CreatedTokenResponse:
        """
        Resource /v2/{merchantId}/tokens - Create token

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CreateTokenApi

        :param body: :class:`ingenico.direct.sdk.domain.create_token_request.CreateTokenRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.created_token_response.CreatedTokenResponse`
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
    def get_token(self, token_id: str, context: CallContext = None) -> TokenResponse:
        """
        Resource /v2/{merchantId}/tokens/{tokenId} - Get token

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetTokenApi

        :param token_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.token_response.TokenResponse`
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
    def delete_token(self, token_id: str, context: CallContext = None) -> None:
        """
        Resource /v2/{merchantId}/tokens/{tokenId} - Delete token

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/DeleteTokenApi

        :param token_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: None
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
