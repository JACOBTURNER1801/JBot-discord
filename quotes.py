class Quotes():
    def __init__(self, quotes):
        self.quotes = quotes

    def modify_quotes(self, quote):
        self.quote = quote
        self.quotes.append(str(quote))

    def print_quotes(self, quotes):
        for quote in range(len(self.quotes)):
            print(quote)
