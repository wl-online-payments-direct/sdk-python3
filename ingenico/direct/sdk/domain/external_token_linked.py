# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject


class ExternalTokenLinked(DataObject):

    __gts_computed_token = None

    @property
    def gts_computed_token(self) -> str:
        """
        | The GTS computed token

        Type: str
        """
        return self.__gts_computed_token

    @gts_computed_token.setter
    def gts_computed_token(self, value: str):
        self.__gts_computed_token = value

    def to_dictionary(self):
        dictionary = super(ExternalTokenLinked, self).to_dictionary()
        if self.gts_computed_token is not None:
            dictionary['GTSComputedToken'] = self.gts_computed_token
        return dictionary

    def from_dictionary(self, dictionary):
        super(ExternalTokenLinked, self).from_dictionary(dictionary)
        if 'GTSComputedToken' in dictionary:
            self.gts_computed_token = dictionary['GTSComputedToken']
        return self
