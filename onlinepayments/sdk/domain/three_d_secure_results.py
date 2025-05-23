# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ThreeDSecureResults(DataObject):

    __acs_transaction_id: Optional[str] = None
    __applied_exemption: Optional[str] = None
    __authentication_status: Optional[str] = None
    __cavv: Optional[str] = None
    __challenge_indicator: Optional[str] = None
    __ds_transaction_id: Optional[str] = None
    __eci: Optional[str] = None
    __exemption_engine_flow: Optional[str] = None
    __flow: Optional[str] = None
    __liability: Optional[str] = None
    __scheme_eci: Optional[str] = None
    __version: Optional[str] = None
    __xid: Optional[str] = None

    @property
    def acs_transaction_id(self) -> Optional[str]:
        """
        | Authenticated Transaction Identifier at the ACS/Issuer.

        Type: str
        """
        return self.__acs_transaction_id

    @acs_transaction_id.setter
    def acs_transaction_id(self, value: Optional[str]) -> None:
        self.__acs_transaction_id = value

    @property
    def applied_exemption(self) -> Optional[str]:
        """
        | Exemption requested and applied in the authorization

        Type: str
        """
        return self.__applied_exemption

    @applied_exemption.setter
    def applied_exemption(self, value: Optional[str]) -> None:
        self.__applied_exemption = value

    @property
    def authentication_status(self) -> Optional[str]:
        """
        | One-letter authentication status returned by DS. Possible values are:
        
        * Y - Authentication succeeded
        * A - Authentication attempted
        * I - Information only, liability shifted to the merchant
        * N - Authentication failed
        * R - Authentication rejected
        * U - Authentication unavailable
        * C - Authentication required

        Type: str
        """
        return self.__authentication_status

    @authentication_status.setter
    def authentication_status(self, value: Optional[str]) -> None:
        self.__authentication_status = value

    @property
    def cavv(self) -> Optional[str]:
        """
        | Cardholder Authentication Verification Value. End-2-end reference generated by the Issuer to recognize that the authentication has taken place.

        Type: str
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value: Optional[str]) -> None:
        self.__cavv = value

    @property
    def challenge_indicator(self) -> Optional[str]:
        """
        | Challenge Indicator used for this transaction. This value might differ from the one sent by the merchant if the card is not supporting it (3DS version 2.1 vs 3DS version 2.2).

        Type: str
        """
        return self.__challenge_indicator

    @challenge_indicator.setter
    def challenge_indicator(self, value: Optional[str]) -> None:
        self.__challenge_indicator = value

    @property
    def ds_transaction_id(self) -> Optional[str]:
        """
        | 3D Secure Directory Server Transaction Identifier used for this transaction.

        Type: str
        """
        return self.__ds_transaction_id

    @ds_transaction_id.setter
    def ds_transaction_id(self, value: Optional[str]) -> None:
        self.__ds_transaction_id = value

    @property
    def eci(self) -> Optional[str]:
        """
        | Indicates Authentication validation results returned after AuthenticationValidation

        Type: str
        """
        return self.__eci

    @eci.setter
    def eci(self, value: Optional[str]) -> None:
        self.__eci = value

    @property
    def exemption_engine_flow(self) -> Optional[str]:
        """
        | Detailed description of the Exemption Engine outcomes

        Type: str
        """
        return self.__exemption_engine_flow

    @exemption_engine_flow.setter
    def exemption_engine_flow(self, value: Optional[str]) -> None:
        self.__exemption_engine_flow = value

    @property
    def flow(self) -> Optional[str]:
        """
        | 3D Secure Flow used during this transaction.

        Type: str
        """
        return self.__flow

    @flow.setter
    def flow(self, value: Optional[str]) -> None:
        self.__flow = value

    @property
    def liability(self) -> Optional[str]:
        """
        | Determines the Fraud liability. Possible values are:
        
        * issuer - Fraud liability shifts to the issuer
        * merchant - Fraud liability with the merchant
        
        | Note: When not filled in Fraud liability is not applicable for the current transaction.

        Type: str
        """
        return self.__liability

    @liability.setter
    def liability(self, value: Optional[str]) -> None:
        self.__liability = value

    @property
    def scheme_eci(self) -> Optional[str]:
        """
        | 3D Secure ECI (Electronic Commerce Indicator) depending on the Scheme. Returned by DS.

        Type: str
        """
        return self.__scheme_eci

    @scheme_eci.setter
    def scheme_eci(self, value: Optional[str]) -> None:
        self.__scheme_eci = value

    @property
    def version(self) -> Optional[str]:
        """
        | 3D Secure Protocol version used during this transaction.

        Type: str
        """
        return self.__version

    @version.setter
    def version(self, value: Optional[str]) -> None:
        self.__version = value

    @property
    def xid(self) -> Optional[str]:
        """
        | Transaction ID for the Authentication

        Type: str
        """
        return self.__xid

    @xid.setter
    def xid(self, value: Optional[str]) -> None:
        self.__xid = value

    def to_dictionary(self) -> dict:
        dictionary = super(ThreeDSecureResults, self).to_dictionary()
        if self.acs_transaction_id is not None:
            dictionary['acsTransactionId'] = self.acs_transaction_id
        if self.applied_exemption is not None:
            dictionary['appliedExemption'] = self.applied_exemption
        if self.authentication_status is not None:
            dictionary['authenticationStatus'] = self.authentication_status
        if self.cavv is not None:
            dictionary['cavv'] = self.cavv
        if self.challenge_indicator is not None:
            dictionary['challengeIndicator'] = self.challenge_indicator
        if self.ds_transaction_id is not None:
            dictionary['dsTransactionId'] = self.ds_transaction_id
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.exemption_engine_flow is not None:
            dictionary['exemptionEngineFlow'] = self.exemption_engine_flow
        if self.flow is not None:
            dictionary['flow'] = self.flow
        if self.liability is not None:
            dictionary['liability'] = self.liability
        if self.scheme_eci is not None:
            dictionary['schemeEci'] = self.scheme_eci
        if self.version is not None:
            dictionary['version'] = self.version
        if self.xid is not None:
            dictionary['xid'] = self.xid
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ThreeDSecureResults':
        super(ThreeDSecureResults, self).from_dictionary(dictionary)
        if 'acsTransactionId' in dictionary:
            self.acs_transaction_id = dictionary['acsTransactionId']
        if 'appliedExemption' in dictionary:
            self.applied_exemption = dictionary['appliedExemption']
        if 'authenticationStatus' in dictionary:
            self.authentication_status = dictionary['authenticationStatus']
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'challengeIndicator' in dictionary:
            self.challenge_indicator = dictionary['challengeIndicator']
        if 'dsTransactionId' in dictionary:
            self.ds_transaction_id = dictionary['dsTransactionId']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'exemptionEngineFlow' in dictionary:
            self.exemption_engine_flow = dictionary['exemptionEngineFlow']
        if 'flow' in dictionary:
            self.flow = dictionary['flow']
        if 'liability' in dictionary:
            self.liability = dictionary['liability']
        if 'schemeEci' in dictionary:
            self.scheme_eci = dictionary['schemeEci']
        if 'version' in dictionary:
            self.version = dictionary['version']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self
