# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.fraud_results import FraudResults
from ingenico.direct.sdk.domain.payment_product840_specific_output import PaymentProduct840SpecificOutput


class RedirectPaymentMethodSpecificOutput(DataObject):
    """
    | Object containing the redirect payment product details
    """

    __fraud_results = None
    __payment_product840_specific_output = None
    __payment_product_id = None
    __token = None

    @property
    def fraud_results(self) -> FraudResults:
        """
        | Object containing the results of the fraud screening

        Type: :class:`ingenico.direct.sdk.domain.fraud_results.FraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: FraudResults):
        self.__fraud_results = value

    @property
    def payment_product840_specific_output(self) -> PaymentProduct840SpecificOutput:
        """
        | PayPal (payment product 840) specific details

        Type: :class:`ingenico.direct.sdk.domain.payment_product840_specific_output.PaymentProduct840SpecificOutput`
        """
        return self.__payment_product840_specific_output

    @payment_product840_specific_output.setter
    def payment_product840_specific_output(self, value: PaymentProduct840SpecificOutput):
        self.__payment_product840_specific_output = value

    @property
    def payment_product_id(self) -> int:
        """
        | Payment product identifier - Please see [payment products](https://support.direct.ingenico.com/documentation/api/reference/index.html#tag/Products) for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int):
        self.__payment_product_id = value

    @property
    def token(self) -> str:
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificOutput, self).to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.payment_product840_specific_output is not None:
            dictionary['paymentProduct840SpecificOutput'] = self.payment_product840_specific_output.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = FraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'paymentProduct840SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificOutput']))
            value = PaymentProduct840SpecificOutput()
            self.payment_product840_specific_output = value.from_dictionary(dictionary['paymentProduct840SpecificOutput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
