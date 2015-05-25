import networkx as nx
from twitterdao import twitterdao
import time
import matplotlib.pyplot as plt
from celery import Celery
import logging

app = Celery()
graph_logger = logging.getLogger("GraphLogger")
graph_logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('GraphLogger.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
graph_logger.addHandler(fh)
graph_logger.addHandler(ch)

@app.task()
def make_graph(user_dao, center_id, depth=3, directional=True):
    history = set()
    social_graph = nx.DiGraph() if directional else nx.Graph()
    last_request_time = time.time()
    crawl_node(user_dao, center_id, social_graph, depth, history, last_request_time)
    return social_graph


def crawl_node(user_dao, root_id, social_graph, depth, history, last_request_time):
    if depth and root_id not in history:
        graph_logger.info("Crawling id {}. Depth: {}".format(root_id, depth))
        depth -= 1
        history.add(root_id)
        friends = user_dao.get_friend_ids_from_user_id(root_id)
        last_request_time = time.time()
        for friend_id in friends:
            social_graph.add_edge(root_id, friend_id)
            crawl_node(user_dao, friend_id, social_graph, depth, history, last_request_time)

if __name__ == "__main__":
    twitter_dao = twitterdao.TwitterDao()
    user_id = twitter_dao.OWNER_ID
    graph = make_graph(twitter_dao, user_id, depth=2)
    nx.draw_networkx(graph)
    plt.show()
    # plt.savefig("social_graph.png")
