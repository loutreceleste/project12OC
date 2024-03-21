import unittest
from unittest.mock import patch
from model.authentication import decode_token
from model.authentication import User, create_jwt, jwt


class TestDecodeToken(unittest.TestCase):

    @patch('model.authentication.jwt.decode')
    def test_decode_token_successful(self, mock_decode):
        token = "your_test_token"
        user = {"secret_key": "your_secret_key"}
        expected_decoded_jwt = {"payload": "test_data"}
        mock_decode.return_value = expected_decoded_jwt

        actual_decoded_jwt = decode_token(token, user)

        mock_decode.assert_called_once_with(
            token, user["secret_key"].encode('utf-8'), algorithms=["HS256"]
        )

        self.assertEqual(actual_decoded_jwt, expected_decoded_jwt)

    @patch('model.authentication.jwt.decode')
    def test_decode_token_jwt_error(self, mock_decode):
        token = "invalid_token"
        user = {"secret_key": "your_secret_key"}
        mock_decode.side_effect = jwt.exceptions.DecodeError

        with self.assertRaises(jwt.exceptions.DecodeError):
            decode_token(token, user)


@patch('database.session.add')
@patch('model.authentication.jwt.encode')
@patch('model.authentication.Fernet.generate_key')
def test_create_jwt(mock_generate_key, mock_encode, mock_add):

    mock_generate_key.return_value = b'test_secret_key'
    mock_encode.return_value = 'test_encoded_jwt'
    user = User(id=1, name_lastname="Axel", department="COM",
                email="axel@gmail.com")

    generated_jwt = create_jwt(user)

    assert generated_jwt == 'test_encoded_jwt'
    assert user.secret_key == 'test_secret_key'
    assert user.token == 'test_encoded_jwt'
    assert not mock_add.called


if __name__ == '__main__':
    unittest.main()
