#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from abc import ABC, abstractmethod
from ingenico.direct.sdk.call_context import CallContext
from ingenico.direct.sdk.domain.create_payout_request import CreatePayoutRequest
from ingenico.direct.sdk.domain.payout_response import PayoutResponse


class IPayoutsClient(ABC):
    """
    Payouts client interface. Thread-safe.
    """

    @abstractmethod
    def create_payout(self, body: CreatePayoutRequest, context: CallContext = None) -> PayoutResponse:
        """
        Resource /v2/{merchantId}/payouts - Create payout

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CreatePayoutApi

        :param body: :class:`ingenico.direct.sdk.domain.create_payout_request.CreatePayoutRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.payout_response.PayoutResponse`
        :raise: DeclinedPayoutException if the Ingenico ePayments platform declined / rejected the payout. The payout result will be available from the exception.
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
    def get_payout(self, payout_id: str, context: CallContext = None) -> PayoutResponse:
        """
        Resource /v2/{merchantId}/payouts/{payoutId} - Get payout

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetPayoutApi

        :param payout_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.payout_response.PayoutResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
