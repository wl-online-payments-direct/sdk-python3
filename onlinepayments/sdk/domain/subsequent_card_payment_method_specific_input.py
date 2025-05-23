# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class SubsequentCardPaymentMethodSpecificInput(DataObject):

    __authorization_mode: Optional[str] = None
    __payment_number: Optional[int] = None
    __scheme_reference_data: Optional[str] = None
    __subsequent_type: Optional[str] = None
    __token: Optional[str] = None
    __transaction_channel: Optional[str] = None

    @property
    def authorization_mode(self) -> Optional[str]:
        """
        | Determines the type of the authorization that will be used. Allowed values:
        
        * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days.
        * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount.
        * SALE - The payment creation results in an authorization that is already captured at the moment of approval.
        
        | Only used with some acquirers, ignored for acquirers that do not support this. In case the acquirer does not allow this to be specified the authorizationMode is 'unspecified', which behaves similar to a final authorization.

        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value: Optional[str]) -> None:
        self.__authorization_mode = value

    @property
    def payment_number(self) -> Optional[int]:
        """
        | This payment's ordinal number in the sequence of payments.  As the payments are numbered from 1 to the totalNumberOfPayments provided at initialization of the sequence in the multiplePaymentInformation container, the allowed values for this field actually depend on whether the initial call to CreatePayment or CreateHostedCheckout led to a payment or not.
        
        * if the initial call led to a payment, since it is implicitly numbered 1, then the allowed values for this field range from 2 to the totalNumberOfPayments.
        * if the initial call did not lead to a payment (e.g. this was a 0 amount operation for authentication), then the allowed values for this field range from 1 to the totalNumberOfPayments.

        Type: int
        """
        return self.__payment_number

    @payment_number.setter
    def payment_number(self, value: Optional[int]) -> None:
        self.__payment_number = value

    @property
    def scheme_reference_data(self) -> Optional[str]:
        """
        | Deprecated: This is the unique Scheme Reference Data from the initial transaction that was performed with a Strong Customer Authentication. In case this value is unknown, a Scheme Reference of an earlier transaction that was part of the same sequence can be used as a fall-back. Still, it is strongly advised to submit this value for any Merchant Initiated Transaction or any recurring transaction (hereby defined as "Subsequent").

        Type: str

        Deprecated; Deprecated
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: Optional[str]) -> None:
        self.__scheme_reference_data = value

    @property
    def subsequent_type(self) -> Optional[str]:
        """
        | Determines the type of the subsequent that will be used. Allowed values:
        
        * Recurring - Transactions processed at fixed, regular intervals not to exceed one year between Transactions, representing an agreement between a cardholder and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account.
        * Unscheduled - A transaction using a stored credential for a fixed or variable amount that does not occur on a scheduled or regularly occurring transaction date, where the cardholder has provided consent for the merchant to initiate one or more future transactions which are not initiated by the cardholder. This transaction type is based on an agreement with the cardholder and is not to be confused with cardholder initiated transactions performed with stored credentials (CITs are in scope of PSD2 whereas UCOF transactions are MITs and thus out of scope).
        * Installment - Installment payments describe a single purchase of goods or services billed to a cardholder in multiple transactions over a period of time agreed by the cardholder and merchant.
        * NoShow - A No-show is a transaction where the merchant is enabled to charge for services which the cardholder entered into an agreement to purchase but did not meet the terms of the agreement.
        * DelayedCharge - A delayed charge is typically used in hotel, cruise lines and vehicle rental payment scenarios to perform a supplemental account charge after original services are rendered.
        * PartialShipment - I-P e-Commerce scenario whereby credentials have been stored to enable subsequent MITs per shipment. For this type of use case, PartialShipment is expected on both the initial CIT and eventual subsequent MITs to complete the order.
        * Resubmission - This is an event that occurs when the original purchase occurred, but the merchant was not able to get authorization at the time the goods or services were provided. This is only applicable to contactless transit transactions.

        Type: str
        """
        return self.__subsequent_type

    @subsequent_type.setter
    def subsequent_type(self, value: Optional[str]) -> None:
        self.__subsequent_type = value

    @property
    def token(self) -> Optional[str]:
        """
        | Deprecated: ID of the token to use to create the payment.

        Type: str

        Deprecated; ID of the token to use to create the payment.
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    @property
    def transaction_channel(self) -> Optional[str]:
        """
        | Indicates the channel via which the payment is created. Allowed values:
        
        * ECOMMERCE - The transaction is a regular E-Commerce transaction.
        * MOTO - The transaction is a Mail Order/Telephone Order.
        
        | Defaults to ECOMMERCE.

        Type: str
        """
        return self.__transaction_channel

    @transaction_channel.setter
    def transaction_channel(self, value: Optional[str]) -> None:
        self.__transaction_channel = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubsequentCardPaymentMethodSpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.payment_number is not None:
            dictionary['paymentNumber'] = self.payment_number
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.subsequent_type is not None:
            dictionary['subsequentType'] = self.subsequent_type
        if self.token is not None:
            dictionary['token'] = self.token
        if self.transaction_channel is not None:
            dictionary['transactionChannel'] = self.transaction_channel
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentCardPaymentMethodSpecificInput':
        super(SubsequentCardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'paymentNumber' in dictionary:
            self.payment_number = dictionary['paymentNumber']
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'subsequentType' in dictionary:
            self.subsequent_type = dictionary['subsequentType']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'transactionChannel' in dictionary:
            self.transaction_channel = dictionary['transactionChannel']
        return self
