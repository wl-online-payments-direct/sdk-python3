# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject


class PaymentProductDisplayHints(DataObject):
    """
    | Object containing display hints like the order of the product when shown in a list, the name of the product and the logo
    """

    __display_order = None
    __label = None
    __logo = None

    @property
    def display_order(self) -> int:
        """
        Type: int
        """
        return self.__display_order

    @display_order.setter
    def display_order(self, value: int):
        self.__display_order = value

    @property
    def label(self) -> str:
        """
        Type: str
        """
        return self.__label

    @label.setter
    def label(self, value: str):
        self.__label = value

    @property
    def logo(self) -> str:
        """
        Type: str
        """
        return self.__logo

    @logo.setter
    def logo(self, value: str):
        self.__logo = value

    def to_dictionary(self):
        dictionary = super(PaymentProductDisplayHints, self).to_dictionary()
        if self.display_order is not None:
            dictionary['displayOrder'] = self.display_order
        if self.label is not None:
            dictionary['label'] = self.label
        if self.logo is not None:
            dictionary['logo'] = self.logo
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductDisplayHints, self).from_dictionary(dictionary)
        if 'displayOrder' in dictionary:
            self.display_order = dictionary['displayOrder']
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
