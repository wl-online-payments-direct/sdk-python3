# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject


class SessionRequest(DataObject):

    def to_dictionary(self):
        dictionary = super(SessionRequest, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(SessionRequest, self).from_dictionary(dictionary)
        return self
