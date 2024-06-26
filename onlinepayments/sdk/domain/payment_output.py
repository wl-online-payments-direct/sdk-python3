# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card_payment_method_specific_output import CardPaymentMethodSpecificOutput
from onlinepayments.sdk.domain.customer_output import CustomerOutput
from onlinepayments.sdk.domain.discount import Discount
from onlinepayments.sdk.domain.mobile_payment_method_specific_output import MobilePaymentMethodSpecificOutput
from onlinepayments.sdk.domain.payment_references import PaymentReferences
from onlinepayments.sdk.domain.redirect_payment_method_specific_output import RedirectPaymentMethodSpecificOutput
from onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_output import SepaDirectDebitPaymentMethodSpecificOutput
from onlinepayments.sdk.domain.surcharge_specific_output import SurchargeSpecificOutput


class PaymentOutput(DataObject):
    """
    | Object containing payment details
    """

    __acquired_amount = None
    __amount_of_money = None
    __amount_paid = None
    __card_payment_method_specific_output = None
    __customer = None
    __discount = None
    __merchant_parameters = None
    __mobile_payment_method_specific_output = None
    __payment_method = None
    __redirect_payment_method_specific_output = None
    __references = None
    __sepa_direct_debit_payment_method_specific_output = None
    __surcharge_specific_output = None

    @property
    def acquired_amount(self) -> AmountOfMoney:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__acquired_amount

    @acquired_amount.setter
    def acquired_amount(self, value: AmountOfMoney):
        self.__acquired_amount = value

    @property
    def amount_of_money(self) -> AmountOfMoney:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney):
        self.__amount_of_money = value

    @property
    def amount_paid(self) -> int:
        """
        | Amount that has been paid. This is deprecated. Use acquiredAmount instead.

        Type: int
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value: int):
        self.__amount_paid = value

    @property
    def card_payment_method_specific_output(self) -> CardPaymentMethodSpecificOutput:
        """
        | Object containing the card payment method details

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_output.CardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value: CardPaymentMethodSpecificOutput):
        self.__card_payment_method_specific_output = value

    @property
    def customer(self) -> CustomerOutput:
        """
        | Object containing the details of the customer

        Type: :class:`onlinepayments.sdk.domain.customer_output.CustomerOutput`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: CustomerOutput):
        self.__customer = value

    @property
    def discount(self) -> Discount:
        """
        | Object to apply a discount to the total basket by adding a discount line.

        Type: :class:`onlinepayments.sdk.domain.discount.Discount`
        """
        return self.__discount

    @discount.setter
    def discount(self, value: Discount):
        self.__discount = value

    @property
    def merchant_parameters(self) -> str:
        """
        | It allows you to store additional parameters for the transaction in the format you prefer (e.g.-> key-value query string, JSON, etc.) These parameters are then echoed back to you in API GET calls and Webhook notifications. This field must not contain any personal data.

        Type: str
        """
        return self.__merchant_parameters

    @merchant_parameters.setter
    def merchant_parameters(self, value: str):
        self.__merchant_parameters = value

    @property
    def mobile_payment_method_specific_output(self) -> MobilePaymentMethodSpecificOutput:
        """
        | Object containing the mobile payment method details

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_specific_output.MobilePaymentMethodSpecificOutput`
        """
        return self.__mobile_payment_method_specific_output

    @mobile_payment_method_specific_output.setter
    def mobile_payment_method_specific_output(self, value: MobilePaymentMethodSpecificOutput):
        self.__mobile_payment_method_specific_output = value

    @property
    def payment_method(self) -> str:
        """
        | Payment method identifier used by the our payment engine.

        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: str):
        self.__payment_method = value

    @property
    def redirect_payment_method_specific_output(self) -> RedirectPaymentMethodSpecificOutput:
        """
        | Object containing the redirect payment product details

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_method_specific_output.RedirectPaymentMethodSpecificOutput`
        """
        return self.__redirect_payment_method_specific_output

    @redirect_payment_method_specific_output.setter
    def redirect_payment_method_specific_output(self, value: RedirectPaymentMethodSpecificOutput):
        self.__redirect_payment_method_specific_output = value

    @property
    def references(self) -> PaymentReferences:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: PaymentReferences):
        self.__references = value

    @property
    def sepa_direct_debit_payment_method_specific_output(self) -> SepaDirectDebitPaymentMethodSpecificOutput:
        """
        | Object containing the SEPA direct debit details

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_output.SepaDirectDebitPaymentMethodSpecificOutput`
        """
        return self.__sepa_direct_debit_payment_method_specific_output

    @sepa_direct_debit_payment_method_specific_output.setter
    def sepa_direct_debit_payment_method_specific_output(self, value: SepaDirectDebitPaymentMethodSpecificOutput):
        self.__sepa_direct_debit_payment_method_specific_output = value

    @property
    def surcharge_specific_output(self) -> SurchargeSpecificOutput:
        """
        | Object containing specific surcharging attributes applied to an order.

        Type: :class:`onlinepayments.sdk.domain.surcharge_specific_output.SurchargeSpecificOutput`
        """
        return self.__surcharge_specific_output

    @surcharge_specific_output.setter
    def surcharge_specific_output(self, value: SurchargeSpecificOutput):
        self.__surcharge_specific_output = value

    def to_dictionary(self):
        dictionary = super(PaymentOutput, self).to_dictionary()
        if self.acquired_amount is not None:
            dictionary['acquiredAmount'] = self.acquired_amount.to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.amount_paid is not None:
            dictionary['amountPaid'] = self.amount_paid
        if self.card_payment_method_specific_output is not None:
            dictionary['cardPaymentMethodSpecificOutput'] = self.card_payment_method_specific_output.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.discount is not None:
            dictionary['discount'] = self.discount.to_dictionary()
        if self.merchant_parameters is not None:
            dictionary['merchantParameters'] = self.merchant_parameters
        if self.mobile_payment_method_specific_output is not None:
            dictionary['mobilePaymentMethodSpecificOutput'] = self.mobile_payment_method_specific_output.to_dictionary()
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.redirect_payment_method_specific_output is not None:
            dictionary['redirectPaymentMethodSpecificOutput'] = self.redirect_payment_method_specific_output.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_output is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificOutput'] = self.sepa_direct_debit_payment_method_specific_output.to_dictionary()
        if self.surcharge_specific_output is not None:
            dictionary['surchargeSpecificOutput'] = self.surcharge_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentOutput, self).from_dictionary(dictionary)
        if 'acquiredAmount' in dictionary:
            if not isinstance(dictionary['acquiredAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acquiredAmount']))
            value = AmountOfMoney()
            self.acquired_amount = value.from_dictionary(dictionary['acquiredAmount'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = CustomerOutput()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'discount' in dictionary:
            if not isinstance(dictionary['discount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['discount']))
            value = Discount()
            self.discount = value.from_dictionary(dictionary['discount'])
        if 'merchantParameters' in dictionary:
            self.merchant_parameters = dictionary['merchantParameters']
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = MobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'redirectPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificOutput']))
            value = RedirectPaymentMethodSpecificOutput()
            self.redirect_payment_method_specific_output = value.from_dictionary(dictionary['redirectPaymentMethodSpecificOutput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'sepaDirectDebitPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificOutput']))
            value = SepaDirectDebitPaymentMethodSpecificOutput()
            self.sepa_direct_debit_payment_method_specific_output = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'])
        if 'surchargeSpecificOutput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificOutput']))
            value = SurchargeSpecificOutput()
            self.surcharge_specific_output = value.from_dictionary(dictionary['surchargeSpecificOutput'])
        return self
