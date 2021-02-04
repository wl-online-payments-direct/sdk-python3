#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.api_resource import ApiResource
from ingenico.direct.sdk.call_context import CallContext
from ingenico.direct.sdk.response_exception import ResponseException
from ingenico.direct.sdk.domain.error_response import ErrorResponse
from ingenico.direct.sdk.domain.get_payment_product_groups_response import GetPaymentProductGroupsResponse
from ingenico.direct.sdk.domain.payment_product_group import PaymentProductGroup
from ingenico.direct.sdk.merchant.productgroups.get_product_group_params import GetProductGroupParams
from ingenico.direct.sdk.merchant.productgroups.get_product_groups_params import GetProductGroupsParams
from ingenico.direct.sdk.merchant.productgroups.i_product_groups_client import IProductGroupsClient


class ProductGroupsClient(ApiResource, IProductGroupsClient):
    """
    ProductGroups client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.direct.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(ProductGroupsClient, self).__init__(parent, path_context)

    def get_product_groups(self, query: GetProductGroupsParams, context: CallContext = None) -> GetPaymentProductGroupsResponse:
        """
        Resource /v2/{merchantId}/productgroups - Get product groups

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetProductGroups

        :param query: :class:`ingenico.direct.sdk.merchant.productgroups.get_product_groups_params.GetProductGroupsParams`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.get_payment_product_groups_response.GetPaymentProductGroupsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v2/{merchantId}/productgroups", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    GetPaymentProductGroupsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_product_group(self, payment_product_group_id: str, query: GetProductGroupParams, context: CallContext = None) -> PaymentProductGroup:
        """
        Resource /v2/{merchantId}/productgroups/{paymentProductGroupId} - Get product group

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetProductGroup

        :param payment_product_group_id: str
        :param query: :class:`ingenico.direct.sdk.merchant.productgroups.get_product_group_params.GetProductGroupParams`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.payment_product_group.PaymentProductGroup`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentProductGroupId": payment_product_group_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/productgroups/{paymentProductGroupId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductGroup,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
