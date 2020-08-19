# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject


class AccountOnFileAttribute(DataObject):

    __key = None
    __must_write_reason = None
    __status = None
    __value = None

    @property
    def key(self) -> str:
        """
        Type: str
        """
        return self.__key

    @key.setter
    def key(self, value: str):
        self.__key = value

    @property
    def must_write_reason(self) -> str:
        """
        Type: str
        """
        return self.__must_write_reason

    @must_write_reason.setter
    def must_write_reason(self, value: str):
        self.__must_write_reason = value

    @property
    def status(self) -> str:
        """
        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def value(self) -> str:
        """
        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(AccountOnFileAttribute, self).to_dictionary()
        if self.key is not None:
            dictionary['key'] = self.key
        if self.must_write_reason is not None:
            dictionary['mustWriteReason'] = self.must_write_reason
        if self.status is not None:
            dictionary['status'] = self.status
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFileAttribute, self).from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'mustWriteReason' in dictionary:
            self.must_write_reason = dictionary['mustWriteReason']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self
