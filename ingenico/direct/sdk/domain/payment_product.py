# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.payment_product_display_hints import PaymentProductDisplayHints


class PaymentProduct(DataObject):
    """
    | Payment product
    """

    __allows_recurring = None
    __allows_tokenization = None
    __display_hints = None
    __id = None
    __max_amount = None
    __min_amount = None
    __payment_method = None
    __payment_product_group = None
    __uses_redirection_to3rd_party = None

    @property
    def allows_recurring(self) -> bool:
        """
        | Indicates if the product supports recurring payments
        | * true - This payment product supports recurring payments
        | * false - This payment product does not support recurring transactions and can only be used for one-off payments

        Type: bool
        """
        return self.__allows_recurring

    @allows_recurring.setter
    def allows_recurring(self, value: bool):
        self.__allows_recurring = value

    @property
    def allows_tokenization(self) -> bool:
        """
        | Indicates if the payment details can be tokenized for future re-use
        | * true - Payment details from payments done with this payment product can be tokenized for future re-use
        | * false - Payment details from payments done with this payment product can not be tokenized

        Type: bool
        """
        return self.__allows_tokenization

    @allows_tokenization.setter
    def allows_tokenization(self, value: bool):
        self.__allows_tokenization = value

    @property
    def display_hints(self) -> PaymentProductDisplayHints:
        """
        | Object containing display hints like the order of the product when shown in a list, the name of the product and the logo

        Type: :class:`ingenico.direct.sdk.domain.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: PaymentProductDisplayHints):
        self.__display_hints = value

    @property
    def id(self) -> int:
        """
        | The ID of the payment product in our system

        Type: int
        """
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def max_amount(self) -> int:
        """
        | Maximum amount in EUR cents (using 2 decimals, so 1 EUR becomes 100 cents) for transactions done with this payment product

        Type: int
        """
        return self.__max_amount

    @max_amount.setter
    def max_amount(self, value: int):
        self.__max_amount = value

    @property
    def min_amount(self) -> int:
        """
        | Minimum amount in EUR cents (using 2 decimals, so 1 EUR becomes 100 cents) for transactions done with this payment product

        Type: int
        """
        return self.__min_amount

    @min_amount.setter
    def min_amount(self, value: int):
        self.__min_amount = value

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
    def payment_product_group(self) -> str:
        """
        | The payment product group that has this payment product, if there is any. Not populated otherwise. Currently only one payment product group is supported:
        | * cards

        Type: str
        """
        return self.__payment_product_group

    @payment_product_group.setter
    def payment_product_group(self, value: str):
        self.__payment_product_group = value

    @property
    def uses_redirection_to3rd_party(self) -> bool:
        """
        | Indicates whether the payment product requires redirection to a third party to complete the payment. You can use this to filter out products that require a redirect if you don't want to support that.
        | * true - Redirection is required
        | * false - No redirection is required

        Type: bool
        """
        return self.__uses_redirection_to3rd_party

    @uses_redirection_to3rd_party.setter
    def uses_redirection_to3rd_party(self, value: bool):
        self.__uses_redirection_to3rd_party = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct, self).to_dictionary()
        if self.allows_recurring is not None:
            dictionary['allowsRecurring'] = self.allows_recurring
        if self.allows_tokenization is not None:
            dictionary['allowsTokenization'] = self.allows_tokenization
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.max_amount is not None:
            dictionary['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            dictionary['minAmount'] = self.min_amount
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.payment_product_group is not None:
            dictionary['paymentProductGroup'] = self.payment_product_group
        if self.uses_redirection_to3rd_party is not None:
            dictionary['usesRedirectionTo3rdParty'] = self.uses_redirection_to3rd_party
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct, self).from_dictionary(dictionary)
        if 'allowsRecurring' in dictionary:
            self.allows_recurring = dictionary['allowsRecurring']
        if 'allowsTokenization' in dictionary:
            self.allows_tokenization = dictionary['allowsTokenization']
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'maxAmount' in dictionary:
            self.max_amount = dictionary['maxAmount']
        if 'minAmount' in dictionary:
            self.min_amount = dictionary['minAmount']
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'paymentProductGroup' in dictionary:
            self.payment_product_group = dictionary['paymentProductGroup']
        if 'usesRedirectionTo3rdParty' in dictionary:
            self.uses_redirection_to3rd_party = dictionary['usesRedirectionTo3rdParty']
        return self
