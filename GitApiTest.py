#Arpit Patel
#The following code is to test the GitApi file.

import unittest
from GitApi import get_repos, retrieve_commits


class TestGitHubAPI(unittest.TestCase):

    def test_1_Repo(self):
        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 4, "User 'richkempinski' has 4 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)


    def test_4_Commits(self):
        self.assertGreaterEqual(retrieve_commits('richkempinski', 'threads_of_life'), 1)

    def test_5_invalid_user(self):
        self.assertEqual(get_repos("aervnoDNJsdvn"), [])
        self.assertEqual(get_repos("awnonebjnivk a"), [])
        self.assertEqual(get_repos("svnsna egv n "), [])