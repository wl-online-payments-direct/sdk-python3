# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.card_without_cvv import CardWithoutCvv


class CreatedTokenResponse(DataObject):

    __card = None
    __is_new_token = None
    __token = None

    @property
    def card(self) -> CardWithoutCvv:
        """
        Type: :class:`ingenico.direct.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value: CardWithoutCvv):
        self.__card = value

    @property
    def is_new_token(self) -> bool:
        """
        | Indicates if a new token was created 
        |  * true - A new token was created 
        |  * false - A token with the same card number already exists and is returned. Please note that the existing token has not been updated. When you want to update other data then the card number, you need to update data stored in the token explicitly, as data is never updated during the creation of a token.

        Type: bool
        """
        return self.__is_new_token

    @is_new_token.setter
    def is_new_token(self, value: bool):
        self.__is_new_token = value

    @property
    def token(self) -> str:
        """
        | ID of the token

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    def to_dictionary(self):
        dictionary = super(CreatedTokenResponse, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.is_new_token is not None:
            dictionary['isNewToken'] = self.is_new_token
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatedTokenResponse, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
        if 'isNewToken' in dictionary:
            self.is_new_token = dictionary['isNewToken']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
