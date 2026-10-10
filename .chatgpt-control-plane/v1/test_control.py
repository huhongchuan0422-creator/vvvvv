import unittest
from control import status


class ControlPlaneV1Test(unittest.TestCase):
    def test_status(self):
        self.assertEqual(status(), "CHATGPT_GITHUB_LOOP_PASS")


if __name__ == "__main__":
    unittest.main()
