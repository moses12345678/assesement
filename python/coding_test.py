from coding import get_path_extension
import unittest


class CodingTests(unittest.TestCase):

    def test_get_path_extension(self):
        self.assertEqual(".m", get_path_extension("myfile.m"))
        self.assertEqual(".mp4", get_path_extension("myfile.mp4"))
        self.assertEqual(".tl", get_path_extension(
            "/origin/log.user/documents/private/myfile.tl"))
        # add a test to check that we expect an Exception to be raised if None is passed to get_path_extension
        # add a test to check that an exception is raised is an empty string is passed to get_path_extension


if __name__ == '__main__':
    unittest.main()
