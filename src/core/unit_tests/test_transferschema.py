from unittest import TestCase

from src.core.transfer_schema import TransferSchema

class TestTransferSchema(TestCase):
    """
    Unittests for Transferschema
    """

    def test_config_file_not_exist(self):
        """
        Expected non existing dir
        :return:
        """
        raise NotImplementedError

    def test_config_file_not_yaml(self):
        """
        Expected file not yaml
        :return:
        """
        raise NotImplementedError

    def test_sources_valid(self):
        """
        Given a valid schema, expect to be validated correctly
        :return:
        """
        test_transfer_schema = TransferSchema("./config.yml")
        test_transfer_schema.load()
        self.assertNotEqual(None, test_transfer_schema.validate_sources())

    def test_destinations(self):
        pass

    def test_mappings(self):
        pass

    def test_transfers(self):
        pass