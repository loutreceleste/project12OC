import unittest
from unittest.mock import Mock
from model.principal import User
from unittest.mock import patch


class TestFindUser(unittest.TestCase):

    def test_find_user(self):
        user1 = Mock(id=0, name_lastname="Axel", department="COM",
                     email="axel@gmail.com")
        user2 = Mock(id=1, name_lastname="Kevin", department="GES",
                     email="kevin@gmail.com")

        mock_session = Mock()
        mock_session.query.return_value = Mock()
        mock_session.query.return_value.all.return_value = [user1, user2]

        with patch('model.principal.session', mock_session):
            users = User.find_user()

            self.assertIsInstance(users, list)
            self.assertEqual(len(users), 2)
            self.assertEqual(users[0].name_lastname, "Axel")
            self.assertEqual(users[1].name_lastname, "Kevin")


class TestFindUserBySearch(unittest.TestCase):
    def test_find_user_by_search_single_user(self):
        expected_user = Mock(id=0, name_lastname="Axel", department="COM",
                             email="axel@gmail.com")

        mock_session = Mock()

        mock_session.query.return_value.filter.return_value.all.return_value \
            = [expected_user]

        with patch('model.principal.session', mock_session):
            found_users = User.find_user_by_search("Axel")

            self.assertIsInstance(found_users, list)
            self.assertEqual(len(found_users), 1)
            self.assertEqual(found_users[0], expected_user)


if __name__ == '__main__':
    unittest.main()
