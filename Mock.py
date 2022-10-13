"""
Arpit Patel

"""
from GitApi import get_repos, retrieve_commits
from unittest.mock import mock
import unittest


class MockGitHubAPI(unittest.TestCase):

    @mock.patch('GitApi.get_repos')
    def mock_get_repos_1(self, mock_repo_names):
        mock_repo_names.return_value = ['hellowgitworld', 'helloworld', 'project1','threads-of-life']

        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 4, "User 'richkempinski' has 4 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)



    @mock.patch('githubAPI.get_repos')
    def mock_invalid_user(self, mock_repo_name):
        mock_repo_name.return_value = []
        repos = get_repos('sdvnjnWfassvav')
        self.assertEqual(len(repos), 0, "Error: Invalid Username")


if __name__ == '__main__':
    print("Unit Test: Start")
    unittest.main()
