import unittest
from unittest.mock import patch, Mock
from model.principal import Customer

def create_mock_session_all():
    customer1 = Mock(id=1)
    customer1.name = "Valentin"
    customer1.email = "valentin@gmail.com"

    customer2 = Mock(id=2)
    customer2.name = "Kevin"
    customer2.email = "kevin@gmail.com"

    mock_session = Mock()
    mock_session.query.return_value.all.return_value = [customer1, customer2]
    return mock_session

def create_mock_session_search():
    customer1 = Mock(id=0, name_lastname="Valentin", email="valentin@gmail.com", business_name="Carré Noir")

    mock_session = Mock()
    mock_session.query.return_value = Mock()
    mock_session.query.return_value.join.return_value.filter.return_value.all.return_value = [customer1]
    return mock_session

class TestFindCustomer(unittest.TestCase):

    def test_find_customer(self):
        mock_session = create_mock_session_all()

        with patch('model.principal.session', mock_session):

            customers = Customer.find_customer()

            self.assertIsInstance(customers, list)
            self.assertEqual(len(customers), 2)

            self.assertEqual(customers[0].id, 1)
            self.assertEqual(customers[0].name, "Valentin")
            self.assertEqual(customers[0].email, "valentin@gmail.com")

            self.assertEqual(customers[1].id, 2)
            self.assertEqual(customers[1].name, "Kevin")
            self.assertEqual(customers[1].email, "kevin@gmail.com")

class TestFindCustomerBySearch(unittest.TestCase):

    def test_find_customer_by_search(self):
        mock_session = create_mock_session_search()

        with patch('model.principal.session', mock_session):
            customers = Customer.find_customer_by_search("Valentin")

            self.assertIsInstance(customers, list)
            self.assertEqual(len(customers), 1)
            self.assertEqual(customers[0].id, 0)
            self.assertEqual(customers[0].name_lastname, "Valentin")
            self.assertEqual(customers[0].email, "valentin@gmail.com")
            self.assertEqual(customers[0].business_name, "Carré Noir")

if __name__ == '__main__':
    unittest.main()
