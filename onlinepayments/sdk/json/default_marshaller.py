from json import dumps, loads
from typing import Any, Type, Union

from .marshaller import Marshaller, T
from .marshaller_syntax_exception import MarshallerSyntaxException

from onlinepayments.sdk.domain.data_object import DataObject


class DefaultMarshaller(Marshaller):
    """
    Marshaller implementation based on json.
    """

    @staticmethod
    def instance() -> 'DefaultMarshaller':
        return _DEFAULT_MARSHALLER_INSTANCE

    def marshal(self, request_object: Any) -> str:
        if isinstance(request_object, DataObject):
            dictionary = request_object.to_dictionary()
            return dumps(dictionary,
                         default=lambda o: o.to_dictionary(),
                         indent=4)
        else:
            return dumps(request_object,
                         default=lambda o: o.__dict__,
                         indent=4)

    def unmarshal(self, response_json: Union[str, bytes, None], type_class: Type[T]) -> T:
        if not response_json:
            return None
        if issubclass(type_class, DataObject):
            try:
                return type_class().from_dictionary(loads(response_json))
            except ValueError as e:
                raise MarshallerSyntaxException(e) from e

        class Object(object):
            pass

        def convert_to_object(d):
            try:
                d = dict(d)
            except (TypeError, ValueError):
                return d
            o = Object()
            for key, value in d.items():
                o.__dict__[key] = convert_to_object(value)
            return o

        try:
            dictionary = loads(response_json)
            converted_object = convert_to_object(dictionary)
            return converted_object
        except ValueError as e:
            raise MarshallerSyntaxException(e) from e


_DEFAULT_MARSHALLER_INSTANCE = DefaultMarshaller()
