import unittest
from unittest.mock import patch

from ross.http import make_request
from ross.exceptions import RossHTTPNot200


class RossHTTPTestCase(unittest.TestCase):
    @patch("ross.http.requests.get")
    def test_make_request(self, mock_get):
        # mock a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"foo": "bar"}

        response = make_request("http://example.com", retry=1)

        # assertions to ensure the mocked requests.get was used correctly
        mock_get.assert_called_once_with(
            "http://example.com",
            proxies={"http": "127.0.0.1:8118", "https": "127.0.0.1:8118"},
        )
        self.assertEqual(response.status_code, 200)

    @patch(
        "ross.http.requests.get"
    )  # Correctly patching requests.get in the ross.http namespace
    def test_make_request_raises_exception(self, mock_get):
        # mock a failed response
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"foo": "bar"}

        # assertion exception being raised
        with self.assertRaises(RossHTTPNot200):
            make_request("http://example.com", retry=2)


if __name__ == "__main__":
    unittest.main()
