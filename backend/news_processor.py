import spacy
import csv

nlp = spacy.load("en_core_web_sm")

news = """
A major port strike in Germany has disrupted automobile
supply chains. BMW reported delays in receiving raw materials
from China.
"""

doc = nlp(news)

with open("data/processed/news_entities.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Entity", "Type"])

    for entity in doc.ents:
        writer.writerow([entity.text, entity.label_])

print("News entities saved successfully!")