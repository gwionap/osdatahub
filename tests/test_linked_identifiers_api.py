import pytest

from osdatahub import LinkedIdentifiersAPI
from tests.data import linked_identifiers_api_data as data


class TestLinkedIdentifiersAPI:
    @pytest.mark.parametrize(*data.test_get_endpoint())
    def test_get_endpoint(self, key, identifier, feature_type, identifier_type, expected_result):
        # Arrange
        li_api = LinkedIdentifiersAPI(key)
        
        endpoint = li_api._LinkedIdentifiersAPI__get_endpoint(identifier,
                                                              feature_type,
                                                              identifier_type)

        # Assert
        assert endpoint == expected_result
    
    def test_get_endpoint_error(self):
        # Arrange
        li_api = LinkedIdentifiersAPI("KEY")
        
        with pytest.raises(ValueError) as exc_info:   
            endpoint = li_api._LinkedIdentifiersAPI__get_endpoint("ID",
                                                              "featureType",
                                                              "identifierType")
        # Assert  
        assert str(exc_info.value) == "It is possible to query by the feature_type " +\
                                      "OR the identifier type, but not both"

