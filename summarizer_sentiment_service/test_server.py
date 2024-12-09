import requests

text = '''Liverpool and Chelsea have both started the season strongly under new managers, but who will come out on top when they meet at Anfield on Sunday?

"I did not expect Liverpool to be top but Chelsea have surprised me too, also in a positive way," said BBC Sport's football expert Chris Sutton.

"Chelsea fans must be very happy with their side's performances as well as their results, but Anfield will be a true test of where they are at - in the same way this game will tell us more about Arne Slot's Liverpool side too."

Sutton is making predictions for all 380 Premier League matches this season, against a variety of guests.

For week eight, he takes on legendary boxing manager Kellie Maloney.

Do you agree with their forecasts? You can make your own predictions below.

The most popular scoreline selected for each game is used in the scoreboards and tables at the bottom of this page.
'''

print(requests.post("http://127.0.0.1:8000/analyze_sentiment",
            json={"text":text}).json)

# # testing purpose
# from summarizer_google import summarize_text, analyze_sentiment
# import asyncio

# async def test_services():
#     # print(await summarize_text("This is a test text for summarization."))
#     print(analyze_sentiment("This is a test text for sentiment analysis."))

# asyncio.run(test_services())