#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.api_resource import ApiResource
from ingenico.direct.sdk.merchant.i_merchant_client import IMerchantClient
from ingenico.direct.sdk.merchant.hostedcheckout.hosted_checkout_client import HostedCheckoutClient
from ingenico.direct.sdk.merchant.hostedtokenization.hosted_tokenization_client import HostedTokenizationClient
from ingenico.direct.sdk.merchant.payments.payments_client import PaymentsClient
from ingenico.direct.sdk.merchant.payouts.payouts_client import PayoutsClient
from ingenico.direct.sdk.merchant.productgroups.product_groups_client import ProductGroupsClient
from ingenico.direct.sdk.merchant.products.products_client import ProductsClient
from ingenico.direct.sdk.merchant.services.services_client import ServicesClient
from ingenico.direct.sdk.merchant.sessions.sessions_client import SessionsClient
from ingenico.direct.sdk.merchant.tokens.tokens_client import TokensClient


class MerchantClient(ApiResource, IMerchantClient):
    """
    Merchant client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.direct.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(MerchantClient, self).__init__(parent, path_context)

    def products(self) -> ProductsClient:
        """
        Resource /v2/{merchantId}/products

        :return: :class:`ingenico.direct.sdk.merchant.products.i_products_client.IProductsClient`
        """
        return ProductsClient(self, None)

    def sessions(self) -> SessionsClient:
        """
        Resource /v2/{merchantId}/sessions

        :return: :class:`ingenico.direct.sdk.merchant.sessions.i_sessions_client.ISessionsClient`
        """
        return SessionsClient(self, None)

    def payouts(self) -> PayoutsClient:
        """
        Resource /v2/{merchantId}/payouts

        :return: :class:`ingenico.direct.sdk.merchant.payouts.i_payouts_client.IPayoutsClient`
        """
        return PayoutsClient(self, None)

    def payments(self) -> PaymentsClient:
        """
        Resource /v2/{merchantId}/payments

        :return: :class:`ingenico.direct.sdk.merchant.payments.i_payments_client.IPaymentsClient`
        """
        return PaymentsClient(self, None)

    def services(self) -> ServicesClient:
        """
        Resource /v2/{merchantId}/services

        :return: :class:`ingenico.direct.sdk.merchant.services.i_services_client.IServicesClient`
        """
        return ServicesClient(self, None)

    def product_groups(self) -> ProductGroupsClient:
        """
        Resource /v2/{merchantId}/productgroups

        :return: :class:`ingenico.direct.sdk.merchant.productgroups.i_product_groups_client.IProductGroupsClient`
        """
        return ProductGroupsClient(self, None)

    def hosted_tokenization(self) -> HostedTokenizationClient:
        """
        Resource /v2/{merchantId}/hostedtokenizations

        :return: :class:`ingenico.direct.sdk.merchant.hostedtokenization.i_hosted_tokenization_client.IHostedTokenizationClient`
        """
        return HostedTokenizationClient(self, None)

    def tokens(self) -> TokensClient:
        """
        Resource /v2/{merchantId}/tokens

        :return: :class:`ingenico.direct.sdk.merchant.tokens.i_tokens_client.ITokensClient`
        """
        return TokensClient(self, None)

    def hosted_checkout(self) -> HostedCheckoutClient:
        """
        Resource /v2/{merchantId}/hostedcheckouts

        :return: :class:`ingenico.direct.sdk.merchant.hostedcheckout.i_hosted_checkout_client.IHostedCheckoutClient`
        """
        return HostedCheckoutClient(self, None)
