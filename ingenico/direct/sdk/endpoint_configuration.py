from urllib.parse import urlparse

from ingenico.direct.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from .proxy_configuration import ProxyConfiguration


class EndpointConfiguration:
    """
    Base class for endpoint configurations.
    """
    # The default number of maximum connections.
    DEFAULT_CONNECT_TIMEOUT = 5
    DEFAULT_SOCKET_TIMEOUT = 300
    DEFAULT_MAX_CONNECTIONS = 10

    def __init__(self, properties=None, prefix=None):
        if properties and properties.sections() and properties.options("DirectSDK"):
            self.__endpoint = self.__get_endpoint(properties, prefix)
            self.__connect_timeout = int(properties.get("DirectSDK", prefix + ".connectTimeout", fallback=self.DEFAULT_CONNECT_TIMEOUT))
            self.__socket_timeout = int(properties.get("DirectSDK", prefix + ".socketTimeout", fallback=self.DEFAULT_SOCKET_TIMEOUT))
            self.__max_connections = int(properties.get("DirectSDK", prefix + ".maxConnections", fallback=self.DEFAULT_MAX_CONNECTIONS))
            proxy_uri = properties.get("DirectSDK", prefix + ".proxy.uri", fallback=None)
            if proxy_uri is None:
                self.__proxy_configuration = None
            else:
                self.__proxy_configuration = ProxyConfiguration.from_uri(
                    proxy_uri,
                    properties.get("DirectSDK", prefix + ".proxy.username", fallback=None),
                    properties.get("DirectSDK", prefix + ".proxy.password", fallback=None))
            self.__integrator = properties.get("DirectSDK", prefix + ".integrator", fallback=None)
            self.__shopping_cart_extension = self.__get_shopping_cart_extension(properties, prefix)

    def __get_endpoint(self, properties, prefix):
        host = properties.get("DirectSDK", prefix + ".endpoint.host")
        scheme = properties.get("DirectSDK", prefix + ".endpoint.scheme", fallback="https")
        port = int(properties.get("DirectSDK", prefix + ".endpoint.port", fallback=-1))
        return self.__create_uri(scheme, host, port)

    @staticmethod
    def __create_uri(scheme, host, port):
        if port != -1:
            uri = scheme + "://" + host + ":" + str(port)
        else:
            uri = scheme + "://" + host
        url = urlparse(uri)
        if not url.scheme.lower() in ["http", "https"] or not url.netloc:
            raise ValueError("Unable to construct endpoint URI")
        return url

    @staticmethod
    def __get_shopping_cart_extension(properties, prefix):
        creator = properties.get("DirectSDK", prefix + ".shoppingCartExtension.creator", fallback=None)
        name = properties.get("DirectSDK", prefix + ".shoppingCartExtension.name", fallback=None)
        version = properties.get("DirectSDK", prefix + ".shoppingCartExtension.version", fallback=None)
        extension_id = properties.get("DirectSDK", prefix + ".shoppingCartExtension.extensionId", fallback=None)
        if creator is None and name is None and version is None and extension_id is None:
            return None
        else:
            return ShoppingCartExtension(creator, name, version, extension_id)

    @property
    def _endpoint(self):
        return self.__endpoint

    def _set_endpoint(self, endpoint):
        if isinstance(endpoint, str):
            endpoint = urlparse(str(endpoint))
        if endpoint is not None and endpoint.path:
            raise ValueError("apiEndpoint should not contain a path")
        if endpoint is not None and (
                endpoint.username is not None or
                endpoint.query or endpoint.fragment):
            raise ValueError(
                "apiEndpoint should not contain user info, query or fragment")
        self.__endpoint = endpoint

    @property
    def connect_timeout(self):
        """Connection timeout for the underlying network communication in seconds"""
        return self.__connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        self.__connect_timeout = connect_timeout

    @property
    def socket_timeout(self):
        """Socket timeout for the underlying network communication in seconds"""
        return self.__socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout):
        self.__socket_timeout = socket_timeout

    @property
    def max_connections(self):
        return self.__max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        self.__max_connections = max_connections

    @property
    def proxy_configuration(self):
        return self.__proxy_configuration

    @proxy_configuration.setter
    def proxy_configuration(self, proxy_configuration):
        self.__proxy_configuration = proxy_configuration

    @property
    def integrator(self):
        return self.__integrator

    @integrator.setter
    def integrator(self, integrator):
        self.__integrator = integrator

    @property
    def shopping_cart_extension(self):
        return self.__shopping_cart_extension

    @shopping_cart_extension.setter
    def shopping_cart_extension(self, shopping_cart_extension):
        self.__shopping_cart_extension = shopping_cart_extension
