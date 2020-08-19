# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject


class LabelTemplateElement(DataObject):

    __attribute_key = None
    __mask = None

    @property
    def attribute_key(self) -> str:
        """
        Type: str
        """
        return self.__attribute_key

    @attribute_key.setter
    def attribute_key(self, value: str):
        self.__attribute_key = value

    @property
    def mask(self) -> str:
        """
        Type: str
        """
        return self.__mask

    @mask.setter
    def mask(self, value: str):
        self.__mask = value

    def to_dictionary(self):
        dictionary = super(LabelTemplateElement, self).to_dictionary()
        if self.attribute_key is not None:
            dictionary['attributeKey'] = self.attribute_key
        if self.mask is not None:
            dictionary['mask'] = self.mask
        return dictionary

    def from_dictionary(self, dictionary):
        super(LabelTemplateElement, self).from_dictionary(dictionary)
        if 'attributeKey' in dictionary:
            self.attribute_key = dictionary['attributeKey']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        return self
