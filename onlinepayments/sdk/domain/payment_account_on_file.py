# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentAccountOnFile(DataObject):

    __create_date: Optional[str] = None
    __number_of_card_on_file_creation_attempts_last24_hours: Optional[int] = None

    @property
    def create_date(self) -> Optional[str]:
        """
        | The date (YYYYMMDD) when the payment account on file was first created.
        |
        | In case a token is used for the transaction we will use the creation date of the token in our system in case you leave this property empty.

        Type: str
        """
        return self.__create_date

    @create_date.setter
    def create_date(self, value: Optional[str]) -> None:
        self.__create_date = value

    @property
    def number_of_card_on_file_creation_attempts_last24_hours(self) -> Optional[int]:
        """
        | Number of attempts made to add new card to the customer account in the last 24 hours

        Type: int
        """
        return self.__number_of_card_on_file_creation_attempts_last24_hours

    @number_of_card_on_file_creation_attempts_last24_hours.setter
    def number_of_card_on_file_creation_attempts_last24_hours(self, value: Optional[int]) -> None:
        self.__number_of_card_on_file_creation_attempts_last24_hours = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentAccountOnFile, self).to_dictionary()
        if self.create_date is not None:
            dictionary['createDate'] = self.create_date
        if self.number_of_card_on_file_creation_attempts_last24_hours is not None:
            dictionary['numberOfCardOnFileCreationAttemptsLast24Hours'] = self.number_of_card_on_file_creation_attempts_last24_hours
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentAccountOnFile':
        super(PaymentAccountOnFile, self).from_dictionary(dictionary)
        if 'createDate' in dictionary:
            self.create_date = dictionary['createDate']
        if 'numberOfCardOnFileCreationAttemptsLast24Hours' in dictionary:
            self.number_of_card_on_file_creation_attempts_last24_hours = dictionary['numberOfCardOnFileCreationAttemptsLast24Hours']
        return self
