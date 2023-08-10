# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_filters_hosted_tokenization import PaymentProductFiltersHostedTokenization


class CreateHostedTokenizationRequest(DataObject):
    __ask_consumer_consent = None
    __locale = None
    __payment_product_filters = None
    __tokens = None
    __variant = None

    @property
    def ask_consumer_consent(self) -> bool:
        """
        | Indicate if the tokenization form should contain a checkbox asking the user to give consent for storing their information for future payments.
        | If this parameter is false or missing, you should ask the user yourself and provide their answer when submitting the Tokenizer in your JavaScript code. To pass this choice set the submitTokenization function's parameter storePermanently to false, if you choose not to store the token for subsequent payments, or to true otherwise.

        Type: bool
        """
        return self.__ask_consumer_consent

    @ask_consumer_consent.setter
    def ask_consumer_consent(self, value: bool):
        self.__ask_consumer_consent = value

    @property
    def locale(self) -> str:
        """
        | Locale used in the GUI towards the consumer. 

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: str):
        self.__locale = value

    @property
    def payment_product_filters(self) -> PaymentProductFiltersHostedTokenization:
        """
        | Contains the payment product ids that will be used for manipulating the payment products available for the payment to the customer.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filters_hosted_tokenization.PaymentProductFiltersHostedTokenization`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value: PaymentProductFiltersHostedTokenization):
        self.__payment_product_filters = value

    @property
    def tokens(self) -> str:
        """
        | String containing comma separated tokens (no spaces) associated with the customer of this hosted session. Valid tokens will be used to present the customer the option to re-use previously used payment details. This means the customer for instance does not have to re-enter their card details again, which a big plus when the customer is using their mobile phone to complete the operation.

        Type: str
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: str):
        self.__tokens = value

    @property
    def variant(self) -> str:
        """
        | It is possible to upload multiple templates of your payment pages using the Merchant Portal. You can force the use of a custom template by specifying it in the variant field. This allows you to test out the effect of certain changes to your payment pages in a controlled manner. Please note that you need to specify the filename of the template or customization.

        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value: str):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(CreateHostedTokenizationRequest, self).to_dictionary()
        if self.ask_consumer_consent is not None:
            dictionary['askConsumerConsent'] = self.ask_consumer_consent
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.payment_product_filters is not None:
            dictionary['paymentProductFilters'] = self.payment_product_filters.to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = self.tokens
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedTokenizationRequest, self).from_dictionary(dictionary)
        if 'askConsumerConsent' in dictionary:
            self.ask_consumer_consent = dictionary['askConsumerConsent']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersHostedTokenization()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self
