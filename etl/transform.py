from datetime import datetime
from tqdm import tqdm


class Transform:
    def __init__(self, feednews: dict) -> None:
        self.feednews = feednews
        self.agencias = feednews.keys()

    def transformation(self):
        for agencia in tqdm(self.agencias):
            for feed in self.feednews[agencia]:
                feed["published"] = (
                    self.format_date(feed["published"])
                    if "published" in feed.keys()
                    else None
                )
        return self.feednews

    def format_date(self, string_date: str) -> str:
        try:
            parsed_datetime = datetime.strptime(string_date, "%a, %d %b %Y %H:%M:%S %Z")
            formatted_date_string = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S")

            return formatted_date_string
        except Exception as e:
            return "Invalid Data"
