# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from typing import List

from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.label_template_element import LabelTemplateElement


class AccountOnFileDisplayHints(DataObject):

    __label_template = None
    __logo = None

    @property
    def label_template(self) -> List[LabelTemplateElement]:
        """
        Type: list[:class:`ingenico.direct.sdk.domain.label_template_element.LabelTemplateElement`]
        """
        return self.__label_template

    @label_template.setter
    def label_template(self, value: List[LabelTemplateElement]):
        self.__label_template = value

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
        dictionary = super(AccountOnFileDisplayHints, self).to_dictionary()
        if self.label_template is not None:
            dictionary['labelTemplate'] = []
            for element in self.label_template:
                if element is not None:
                    dictionary['labelTemplate'].append(element.to_dictionary())
        if self.logo is not None:
            dictionary['logo'] = self.logo
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFileDisplayHints, self).from_dictionary(dictionary)
        if 'labelTemplate' in dictionary:
            if not isinstance(dictionary['labelTemplate'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['labelTemplate']))
            self.label_template = []
            for element in dictionary['labelTemplate']:
                value = LabelTemplateElement()
                self.label_template.append(value.from_dictionary(element))
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
