import unittest
from unittest.mock import Mock
from model.principal import User
from unittest.mock import patch

def create_mock_session_all():
    user1 = Mock(id=0, name_lastname="Axel", department="COM", email="axel@gmail.com")
    user2 = Mock(id=1, name_lastname="Kevin", department="GES", email="kevin@gmail.com")

    mock_session = Mock()
    mock_session.query.return_value = Mock()
    mock_session.query.return_value.all.return_value = [user1, user2]
    return mock_session

def create_mock_session_search():
    user1 = Mock(id=0, name_lastname="Axel", department="COM", email="axel@gmail.com")

    mock_session = Mock()
    mock_session.query.return_value.filter.return_value.all.return_value = [user1]
    return mock_session


class TestFindUser(unittest.TestCase):

    def test_find_user(self):
        mock_session = create_mock_session_all()

        with patch('model.principal.session', mock_session):
            users = User.find_user()

            self.assertIsInstance(users, list)

            self.assertEqual(len(users), 2)
            self.assertEqual(users[0].name_lastname, "Axel")
            self.assertEqual(users[1].name_lastname, "Kevin")

class TestFindUserBySearch(unittest.TestCase):

    def test_find_user_by_search(self):
        mock_session = create_mock_session_search()

        with patch('model.principal.session', mock_session):
            users = User.find_user_by_search("Axel")

            self.assertIsInstance(users, list)

            self.assertEqual(len(users), 1)

            self.assertEqual(users[0].id, 0)
            self.assertEqual(users[0].name_lastname, "Axel")
            self.assertEqual(users[0].department, "COM")
            self.assertEqual(users[0].email, "axel@gmail.com")


if __name__ == '__main__':
    unittest.main()
