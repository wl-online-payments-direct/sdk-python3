# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class MandatePersonalNameResponse(DataObject):
    """
    | Object containing the name details of the customer.
    """

    __first_name = None
    __surname = None

    @property
    def first_name(self) -> str:
        """
        | Given name(s) or first name(s) of the customer.

        Type: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = value

    @property
    def surname(self) -> str:
        """
        | Surname(s) or last name(s) of the customer.

        Type: str
        """
        return self.__surname

    @surname.setter
    def surname(self, value: str):
        self.__surname = value

    def to_dictionary(self):
        dictionary = super(MandatePersonalNameResponse, self).to_dictionary()
        if self.first_name is not None:
            dictionary['firstName'] = self.first_name
        if self.surname is not None:
            dictionary['surname'] = self.surname
        return dictionary

    def from_dictionary(self, dictionary):
        super(MandatePersonalNameResponse, self).from_dictionary(dictionary)
        if 'firstName' in dictionary:
            self.first_name = dictionary['firstName']
        if 'surname' in dictionary:
            self.surname = dictionary['surname']
        return self
