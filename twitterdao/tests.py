from django.test import TestCase
from twitterdao import TwitterDao


class TwitterDaoTest(TestCase):
    def setUp(self):
        self.twitter_dao = TwitterDao()

    def test_refresh_token(self):
        self.twitter_dao.refresh_app_access_token()
        is_authenticated = self.twitter_dao.is_app_authenticated()
        self.assertTrue(is_authenticated)

    def test_get_user_id_friends(self):
        user_id = self.twitter_dao.OWNER_ID
        self.twitter_dao.get_friend_ids_from_user_id(user_id)