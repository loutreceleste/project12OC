from unittest.mock import Mock, patch
import unittest
from model.principal import Event


class TestFindEventWithoutSupport(unittest.TestCase):
    def test_find_event_without_support(self):
        mock_session = Mock()

        mock_query = Mock()

        mock_query.filter.return_value.all.return_value = []

        mock_session.query.return_value = mock_query

        with patch('model.principal.session', mock_session):
            events = Event.find_event_without_support()

            self.assertIsInstance(events, list)
            self.assertEqual(len(events), 0)


class TestFindEventBySupport(unittest.TestCase):

    def test_find_event_by_support(self):
        event1 = Mock()
        event1.id = 0
        event1.name = "Mariage"
        event1.description = "Marseille"
        event1.support_contact = "Kevin"

        event2 = Mock()
        event2.id = 1
        event2.name = "Anniversaire"
        event2.description = "La Ciotat"
        event2.support_contact = "Axel"

        mock_query = Mock()
        mock_query.filter.return_value.all.return_value = [event1, event2]
        mock_session = Mock(query=Mock(return_value=mock_query))

        user = Mock(name_lastname="Kevin")

        with patch('model.principal.session', mock_session):
            events = Event.find_event_by_support(user)

            self.assertIsInstance(events, list)
            self.assertEqual(len(events), 2)

            self.assertEqual(events[0].id, 0)
            self.assertEqual(events[0].name, "Mariage")
            self.assertEqual(events[0].description, "Marseille")
            self.assertEqual(events[0].support_contact, "Kevin")


if __name__ == "__main__":
    unittest.main()
