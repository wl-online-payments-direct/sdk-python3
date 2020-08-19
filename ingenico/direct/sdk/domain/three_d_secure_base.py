# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.three_d_secure_data import ThreeDSecureData


class ThreeDSecureBase(DataObject):
    """
    | Object containing specific data regarding 3-D Secure
    """

    __challenge_canvas_size = None
    __challenge_indicator = None
    __exemption_request = None
    __prior_three_d_secure_data = None
    __skip_authentication = None

    @property
    def challenge_canvas_size(self) -> str:
        """
        | Dimensions of the challenge window that potentially will be displayed to the customer. The challenge content is formatted to appropriately render in this window to provide the best possible user experience. Preconfigured sizes are width x height in pixels of the window displayed in the customer browser window. Possible values are
        |    * 250x400 (default)
        |    * 390x400
        |    * 500x600
        |    * 600x400
        |    * full-screen

        Type: str
        """
        return self.__challenge_canvas_size

    @challenge_canvas_size.setter
    def challenge_canvas_size(self, value: str):
        self.__challenge_canvas_size = value

    @property
    def challenge_indicator(self) -> str:
        """
        | Allows you to indicate if you want the customer to be challenged for extra security on this transaction. Possible values:
        |  * no-preference - You have no preference whether or not to challenge the customer (default)
        |  * no-challenge-requested - you prefer the cardholder not to be challenged
        |  * challenge-requested - you prefer the customer to be challenged
        |  * challenge-required - you require the customer to be challenged
        |  * no-challenge-requested-risk-analysis-performed – letting the issuer know that you have already assessed the transaction with fraud prevention tool 
        |  * no-challenge-requested-data-share-only – sharing data only with the DS
        |  * no-challenge-requested-consumer-authentication-performed – authentication already happened at your side – when login in to your website
        |  * no-challenge-requested-use-whitelist-exemption – cardholder has whitelisted you at with the issuer
        |  * challenge-requested-whitelist-prompt-requested – cardholder is trying to whitelist you
        |  * request-scoring-without-connecting-to-acs – sending information to CB DS for a fraud scoring

        Type: str
        """
        return self.__challenge_indicator

    @challenge_indicator.setter
    def challenge_indicator(self, value: str):
        self.__challenge_indicator = value

    @property
    def exemption_request(self) -> str:
        """
        | In PSD2, the ExemptionRequest field is used by merchants requesting an exemption when not using authentication on a transaction, in order to keep the conversion up.
        | * none = No exemption requested
        | * transaction-risk-analysis = Fraud analysis has been done already by your own fraud module and transaction scored as low risk
        | * low-value = Bellow 30 euros
        | * whitelist = The cardholder has whitelisted you with their issuer

        Type: str
        """
        return self.__exemption_request

    @exemption_request.setter
    def exemption_request(self, value: str):
        self.__exemption_request = value

    @property
    def prior_three_d_secure_data(self) -> ThreeDSecureData:
        """
        | Object containing data regarding the customer authentication that occurred prior to the current transaction

        Type: :class:`ingenico.direct.sdk.domain.three_d_secure_data.ThreeDSecureData`
        """
        return self.__prior_three_d_secure_data

    @prior_three_d_secure_data.setter
    def prior_three_d_secure_data(self, value: ThreeDSecureData):
        self.__prior_three_d_secure_data = value

    @property
    def skip_authentication(self) -> bool:
        """
        | * true = 3D Secure authentication will be skipped for this transaction. This setting should be used when isRecurring is set to true and recurringPaymentSequenceIndicator is set to recurring.
        | * false = 3D Secure authentication will not be skipped for this transaction.
        | Note: This is only possible if your account in our system is setup for 3D Secure authentication and if your configuration in our system allows you to override it per transaction.

        Type: bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value: bool):
        self.__skip_authentication = value

    def to_dictionary(self):
        dictionary = super(ThreeDSecureBase, self).to_dictionary()
        if self.challenge_canvas_size is not None:
            dictionary['challengeCanvasSize'] = self.challenge_canvas_size
        if self.challenge_indicator is not None:
            dictionary['challengeIndicator'] = self.challenge_indicator
        if self.exemption_request is not None:
            dictionary['exemptionRequest'] = self.exemption_request
        if self.prior_three_d_secure_data is not None:
            dictionary['priorThreeDSecureData'] = self.prior_three_d_secure_data.to_dictionary()
        if self.skip_authentication is not None:
            dictionary['skipAuthentication'] = self.skip_authentication
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecureBase, self).from_dictionary(dictionary)
        if 'challengeCanvasSize' in dictionary:
            self.challenge_canvas_size = dictionary['challengeCanvasSize']
        if 'challengeIndicator' in dictionary:
            self.challenge_indicator = dictionary['challengeIndicator']
        if 'exemptionRequest' in dictionary:
            self.exemption_request = dictionary['exemptionRequest']
        if 'priorThreeDSecureData' in dictionary:
            if not isinstance(dictionary['priorThreeDSecureData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['priorThreeDSecureData']))
            value = ThreeDSecureData()
            self.prior_three_d_secure_data = value.from_dictionary(dictionary['priorThreeDSecureData'])
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        return self
