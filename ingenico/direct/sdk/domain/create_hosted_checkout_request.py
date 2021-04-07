# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from ingenico.direct.sdk.domain.fraud_fields import FraudFields
from ingenico.direct.sdk.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from ingenico.direct.sdk.domain.mobile_payment_method_hosted_checkout_specific_input import MobilePaymentMethodHostedCheckoutSpecificInput
from ingenico.direct.sdk.domain.order import Order
from ingenico.direct.sdk.domain.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput


class CreateHostedCheckoutRequest(DataObject):

    __card_payment_method_specific_input = None
    __fraud_fields = None
    __hosted_checkout_specific_input = None
    __mobile_payment_method_specific_input = None
    __order = None
    __redirect_payment_method_specific_input = None

    @property
    def card_payment_method_specific_input(self) -> CardPaymentMethodSpecificInputBase:
        """
        | Object containing the specific input details for card payments

        Type: :class:`ingenico.direct.sdk.domain.card_payment_method_specific_input_base.CardPaymentMethodSpecificInputBase`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CardPaymentMethodSpecificInputBase):
        self.__card_payment_method_specific_input = value

    @property
    def fraud_fields(self) -> FraudFields:
        """
        | Object containing additional data that will be used to assess the risk of fraud

        Type: :class:`ingenico.direct.sdk.domain.fraud_fields.FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value: FraudFields):
        self.__fraud_fields = value

    @property
    def hosted_checkout_specific_input(self) -> HostedCheckoutSpecificInput:
        """
        | Object containing hosted checkout specific data

        Type: :class:`ingenico.direct.sdk.domain.hosted_checkout_specific_input.HostedCheckoutSpecificInput`
        """
        return self.__hosted_checkout_specific_input

    @hosted_checkout_specific_input.setter
    def hosted_checkout_specific_input(self, value: HostedCheckoutSpecificInput):
        self.__hosted_checkout_specific_input = value

    @property
    def mobile_payment_method_specific_input(self) -> MobilePaymentMethodHostedCheckoutSpecificInput:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`ingenico.direct.sdk.domain.mobile_payment_method_hosted_checkout_specific_input.MobilePaymentMethodHostedCheckoutSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: MobilePaymentMethodHostedCheckoutSpecificInput):
        self.__mobile_payment_method_specific_input = value

    @property
    def order(self) -> Order:
        """
        | Order object containing order related data 
        |  Please note that this object is required to be able to submit the amount.

        Type: :class:`ingenico.direct.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Order):
        self.__order = value

    @property
    def redirect_payment_method_specific_input(self) -> RedirectPaymentMethodSpecificInput:
        """
        | Object containing the specific input details for payments that involve redirects to 3rd parties to complete, like iDeal and PayPal

        Type: :class:`ingenico.direct.sdk.domain.redirect_payment_method_specific_input.RedirectPaymentMethodSpecificInput`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value: RedirectPaymentMethodSpecificInput):
        self.__redirect_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(CreateHostedCheckoutRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_checkout_specific_input is not None:
            dictionary['hostedCheckoutSpecificInput'] = self.hosted_checkout_specific_input.to_dictionary()
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedCheckoutRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputBase()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'hostedCheckoutSpecificInput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificInput']))
            value = HostedCheckoutSpecificInput()
            self.hosted_checkout_specific_input = value.from_dictionary(dictionary['hostedCheckoutSpecificInput'])
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodHostedCheckoutSpecificInput()
            self.mobile_payment_method_specific_input = value.from_dictionary(dictionary['mobilePaymentMethodSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'redirectPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificInput']))
            value = RedirectPaymentMethodSpecificInput()
            self.redirect_payment_method_specific_input = value.from_dictionary(dictionary['redirectPaymentMethodSpecificInput'])
        return self
