import random


class Quotes():
    # constructor
    def __init__(self, quotes):
        self.quotes = quotes

    # modify the quotes array
    def modify_quotes(self, quote):
        self.quote = quote
        self.quotes.append(str(quote))

    # get a random quote from the array
    def get_quote(self, quotes) -> str:
        random_index = random.randint(1, len(quotes))
        # get the quote (quote is a string)
        quote: str = quotes[random_index]
        return quote

    # display quotes
    def print_quotes(self, quotes):
        for quote in range(len(self.quotes)):
            print(quote)
# end class
