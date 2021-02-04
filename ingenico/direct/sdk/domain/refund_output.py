# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.amount_of_money import AmountOfMoney
from ingenico.direct.sdk.domain.payment_references import PaymentReferences
from ingenico.direct.sdk.domain.refund_card_method_specific_output import RefundCardMethodSpecificOutput
from ingenico.direct.sdk.domain.refund_e_wallet_method_specific_output import RefundEWalletMethodSpecificOutput
from ingenico.direct.sdk.domain.refund_mobile_method_specific_output import RefundMobileMethodSpecificOutput
from ingenico.direct.sdk.domain.refund_redirect_method_specific_output import RefundRedirectMethodSpecificOutput


class RefundOutput(DataObject):
    """
    | Object containing refund details
    """

    __amount_of_money = None
    __amount_paid = None
    __card_refund_method_specific_output = None
    __e_wallet_refund_method_specific_output = None
    __mobile_refund_method_specific_output = None
    __payment_method = None
    __redirect_refund_method_specific_output = None
    __references = None

    @property
    def amount_of_money(self) -> AmountOfMoney:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`ingenico.direct.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney):
        self.__amount_of_money = value

    @property
    def amount_paid(self) -> int:
        """
        Type: int
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value: int):
        self.__amount_paid = value

    @property
    def card_refund_method_specific_output(self) -> RefundCardMethodSpecificOutput:
        """
        Type: :class:`ingenico.direct.sdk.domain.refund_card_method_specific_output.RefundCardMethodSpecificOutput`
        """
        return self.__card_refund_method_specific_output

    @card_refund_method_specific_output.setter
    def card_refund_method_specific_output(self, value: RefundCardMethodSpecificOutput):
        self.__card_refund_method_specific_output = value

    @property
    def e_wallet_refund_method_specific_output(self) -> RefundEWalletMethodSpecificOutput:
        """
        Type: :class:`ingenico.direct.sdk.domain.refund_e_wallet_method_specific_output.RefundEWalletMethodSpecificOutput`
        """
        return self.__e_wallet_refund_method_specific_output

    @e_wallet_refund_method_specific_output.setter
    def e_wallet_refund_method_specific_output(self, value: RefundEWalletMethodSpecificOutput):
        self.__e_wallet_refund_method_specific_output = value

    @property
    def mobile_refund_method_specific_output(self) -> RefundMobileMethodSpecificOutput:
        """
        Type: :class:`ingenico.direct.sdk.domain.refund_mobile_method_specific_output.RefundMobileMethodSpecificOutput`
        """
        return self.__mobile_refund_method_specific_output

    @mobile_refund_method_specific_output.setter
    def mobile_refund_method_specific_output(self, value: RefundMobileMethodSpecificOutput):
        self.__mobile_refund_method_specific_output = value

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
    def redirect_refund_method_specific_output(self) -> RefundRedirectMethodSpecificOutput:
        """
        Type: :class:`ingenico.direct.sdk.domain.refund_redirect_method_specific_output.RefundRedirectMethodSpecificOutput`
        """
        return self.__redirect_refund_method_specific_output

    @redirect_refund_method_specific_output.setter
    def redirect_refund_method_specific_output(self, value: RefundRedirectMethodSpecificOutput):
        self.__redirect_refund_method_specific_output = value

    @property
    def references(self) -> PaymentReferences:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`ingenico.direct.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: PaymentReferences):
        self.__references = value

    def to_dictionary(self):
        dictionary = super(RefundOutput, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.amount_paid is not None:
            dictionary['amountPaid'] = self.amount_paid
        if self.card_refund_method_specific_output is not None:
            dictionary['cardRefundMethodSpecificOutput'] = self.card_refund_method_specific_output.to_dictionary()
        if self.e_wallet_refund_method_specific_output is not None:
            dictionary['eWalletRefundMethodSpecificOutput'] = self.e_wallet_refund_method_specific_output.to_dictionary()
        if self.mobile_refund_method_specific_output is not None:
            dictionary['mobileRefundMethodSpecificOutput'] = self.mobile_refund_method_specific_output.to_dictionary()
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.redirect_refund_method_specific_output is not None:
            dictionary['redirectRefundMethodSpecificOutput'] = self.redirect_refund_method_specific_output.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundOutput, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'cardRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardRefundMethodSpecificOutput']))
            value = RefundCardMethodSpecificOutput()
            self.card_refund_method_specific_output = value.from_dictionary(dictionary['cardRefundMethodSpecificOutput'])
        if 'eWalletRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['eWalletRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eWalletRefundMethodSpecificOutput']))
            value = RefundEWalletMethodSpecificOutput()
            self.e_wallet_refund_method_specific_output = value.from_dictionary(dictionary['eWalletRefundMethodSpecificOutput'])
        if 'mobileRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobileRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobileRefundMethodSpecificOutput']))
            value = RefundMobileMethodSpecificOutput()
            self.mobile_refund_method_specific_output = value.from_dictionary(dictionary['mobileRefundMethodSpecificOutput'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'redirectRefundMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['redirectRefundMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectRefundMethodSpecificOutput']))
            value = RefundRedirectMethodSpecificOutput()
            self.redirect_refund_method_specific_output = value.from_dictionary(dictionary['redirectRefundMethodSpecificOutput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        return self
