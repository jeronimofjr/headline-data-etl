from flask import Flask, render_template, request
import feedparser
from collections import defaultdict
from tqdm import tqdm

from enum import Enum


class Feed(str, Enum):
    BBC = "http://feeds.bbci.co.uk/news/rss.xml"
    CNN = "http://rss.cnn.com/rss/edition.rss"
    FOX = "http://feeds.foxnews.com/foxnews/latest"
    IOL = "http://www.iol.co.za/cmlink/1.640"


class Ingestion:
    def __init__(self) -> None:
        self.keys = ["title", "summary", "link", "id", "published"]
        self.rss_feeds = defaultdict(list)

    def filter(self, news: dict):
        return {att: value for att, value in news.items() if att in self.keys}

    def extract(self):
        for feed in tqdm(iter(Feed)):
            list_news = feedparser.parse(feed.value)["entries"]
            for news in list_news:
                self.rss_feeds[feed.name].append(self.filter(news))
        return self.rss_feeds
