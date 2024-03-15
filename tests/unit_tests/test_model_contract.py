import unittest
from unittest.mock import Mock, patch
from model.principal import Contract, User


class TestFindContract(unittest.TestCase):
    def test_find_contract(self):
        mock_session = Mock()

        contract1 = Mock(id=0, name_lastname="Kevin", total_amount=100)
        contract2 = Mock(id=1, name_lastname="Valentin", total_amount=200)

        mock_session.query.return_value.join.return_value.join.return_value.all.return_value = [contract1, contract2]

        with patch('model.principal.session', mock_session):
            contracts = Contract.find_contract()

            self.assertIsInstance(contracts, list)
            self.assertEqual(len(contracts), 2)
            self.assertEqual(contracts[0].id, 0)
            self.assertEqual(contracts[0].name_lastname, "Kevin")
            self.assertEqual(contracts[0].total_amount, 100)
            self.assertEqual(contracts[1].id, 1)
            self.assertEqual(contracts[1].name_lastname, "Valentin")
            self.assertEqual(contracts[1].total_amount, 200)


class TestFindContractById(unittest.TestCase):
    def test_find_contract_by_id(self):
        mock_session = Mock()

        contract1 = Mock(id=0, description="Contract 1", remaining_amount=50)
        contract2 = Mock(id=1, description="Contract 2", remaining_amount=0)

        mock_session.query.return_value.filter.return_value.first.side_effect = [contract2, contract1]

        with patch('model.principal.session', mock_session):
            contract = Contract.find_contract_by_id(1)

            self.assertEqual(contract.id, 1)
            self.assertEqual(contract.description, "Contract 2")


if __name__ == '__main__':
    unittest.main()


