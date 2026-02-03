import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id": str})

class Receipt:
    def __init__(self, article):
        if article is not None:
            self.article_id = article["id"]
            self.article_name = article["name"]
            self.article_price = article["price"]
        else:
            return None
    
    def generate_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article_name.title()}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)

        pdf.output("receipt.pdf")

class Articles:
    def __init__(self, article_id):
        self.article_id = article_id

    def check_articles_availability(self):
        availability = df.loc[df["id"] == article_id, "in stock"].squeeze()
        if availability.any():
            selected_article = df.loc[df["id"] == article_id].squeeze()
        else:
            selected_article = None
        return selected_article

# pokaz
# wybierz article - Choose an article to buy: po id
## wygeneruj pdf - recept nr id, article: name, price: cena

print(df)
article_id = input("Choose an article to buy: ")
article = Articles(article_id)
selected_article = article.check_articles_availability()
print(selected_article)
if selected_article is not None:
    receipt = Receipt(selected_article)
    receipt.generate_receipt()
else:
    print("Please enter valid article")