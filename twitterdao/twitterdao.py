from os import environ
from base64 import urlsafe_b64encode
import requests
import json
from time import time, sleep
import logging


class TwitterDao():
    APP_ONLY_AUTH_URL = "https://api.twitter.com/oauth2/token"
    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize"
    ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
    CONSUMER_KEY = "CBLwOZ0re3YcYqc4zvuiEPfX5"
    APP_ACCESS_TOKEN = None
    OWNER = "FriendlySavages"
    OWNER_ID = 388064835
    FRIENDS_IDS_URL = "https://api.twitter.com/1.1/friends/ids.json"
    APP_REQUESTS_REMAINING = 15
    log = logging.getLogger(__name__)

    def __init__(self):
        self.SECRET_KEY = environ.get("TWITTER_SECRET_KEY")
        bearer_token_credentials = self.CONSUMER_KEY + ":" + self.SECRET_KEY
        encoded_bearer_token_credentials = urlsafe_b64encode(bearer_token_credentials)
        self.BASIC_AUTH_HEADERS = {'Authorization': 'Basic ' + encoded_bearer_token_credentials}
        self.BEARER_AUTH_HEADERS = None
        self.refresh_app_access_token()

    def refresh_app_access_token(self):
        payload = {'grant_type': 'client_credentials'}
        response = requests.post(self.APP_ONLY_AUTH_URL, headers=self.BASIC_AUTH_HEADERS, params=payload)
        json_response = response.content
        response_dict = json.loads(json_response)
        access_token = response_dict["access_token"]
        self.log.info("New access token: [{}].".format(access_token))
        self.APP_ACCESS_TOKEN = access_token
        self.BEARER_AUTH_HEADERS = {'Authorization': 'Bearer ' + access_token}

    def check_authentication(self):
        if not self.is_app_authenticated():
            self.refresh_app_access_token()

    def is_app_authenticated(self):
        return self.APP_ACCESS_TOKEN is not None

    def get_friend_ids_from_user_id(self, user_id):
        self.check_authentication()
        cursor = -1
        friend_ids = []
        while cursor:
            payload = {'cursor': cursor, 'user_id': user_id}
            self.log.info("Making friend ids request for user  [{}].".format(user_id))
            response = requests.get(self.FRIENDS_IDS_URL, params=payload, headers=self.BEARER_AUTH_HEADERS)
            self.log.info("Made friend ids request for user  [{}].".format(user_id))

            if response.status_code == 401:
                self.log.info("Unauthorized to see friends of user  [{}].".format(user_id))
                break

            headers = response.headers
            self.APP_REQUESTS_REMAINING = int(headers['x-rate-limit-remaining'])
            if not self.APP_REQUESTS_REMAINING:
                self.wait_for_app_window()
            json_response = response.content
            response_dict = json.loads(json_response)
            if "ids" in response_dict:
                ids = response_dict["ids"]
                friend_ids.extend(ids)
            else:
                self.log.warn("Could not find id's in response for twitter id [{}].".format(user_id))

            if "next_cursor" in response_dict:
                cursor = response_dict["next_cursor"]
            else:
                self.log.warn("Could not find cursor in response for twitter id [{}].".format(user_id))
                cursor = 0

        return friend_ids

    def wait_for_app_window(self):
        head_req = requests.head(url=self.FRIENDS_IDS_URL, headers=self.BEARER_AUTH_HEADERS)
        headers = head_req.headers
        self.APP_REQUESTS_REMAINING = int(headers['x-rate-limit-remaining'])
        rate_limit_reset = int(headers['x-rate-limit-reset'])
        current_time = time()
        time_to_wait = rate_limit_reset - current_time
        if time_to_wait > 0:
            self.log.info("Exceeded limit request. Sleeping for  [{}] minutes.".format(time_to_wait/60))
            sleep(time_to_wait)







