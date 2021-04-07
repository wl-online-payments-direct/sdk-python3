# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from typing import List
from ingenico.direct.sdk.data_object import DataObject


class PaymentProduct320SpecificData(DataObject):

    __networks = None

    @property
    def networks(self) -> List[str]:
        """
        | The networks that can be used in the current payment context. The strings that represent the networks in the array are identical to the strings that GooglePay uses in their documentation. For instance "Visa".

        Type: list[str]
        """
        return self.__networks

    @networks.setter
    def networks(self, value: List[str]):
        self.__networks = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct320SpecificData, self).to_dictionary()
        if self.networks is not None:
            dictionary['networks'] = []
            for element in self.networks:
                if element is not None:
                    dictionary['networks'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct320SpecificData, self).from_dictionary(dictionary)
        if 'networks' in dictionary:
            if not isinstance(dictionary['networks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['networks']))
            self.networks = []
            for element in dictionary['networks']:
                self.networks.append(element)
        return self
