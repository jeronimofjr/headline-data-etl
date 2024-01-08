from datetime import datetime
from logging import info
from tqdm import tqdm
import pytz

class Transform:
    def __init__(self, feednews: dict) -> None:
        self.feednews = feednews
        self.presses = feednews.keys()

    def transform(self) -> dict:
        info("Formatação dos dados iniciada!!!")
        for press in tqdm(self.presses):
            for feed in self.feednews[press]:
                feed["published"] = (
                    self.format_date(feed["published"])
                    if "published" in feed.keys()
                    else None
                )
                feed["press"] = press
        return self.feednews

    def format_date(self, string_date: str) -> str:
        try:
            parsed_datetime = datetime.strptime(string_date, "%a, %d %b %Y %H:%M:%S %Z")
            formatted_date_string = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S")

            return formatted_date_string
        except Exception as e:
            return "Invalid Data"
    

    def take_topics(self, topic_model) -> dict:
        corpus = [headline["summary"] for news in self.feednews.values() for headline in news if "summary" in headline.keys()]
        topic = topic_model()
        topics_list = topic.get_topics(corpus)
        return {"topics" : topics_list, "date" : datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%d/%m/%Y %H:%M:%S")}
