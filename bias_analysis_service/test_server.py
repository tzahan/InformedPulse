import requests

text = '''Following President Trump's reelection, left-leaning individuals and organizations are exhibiting widespread disillusionment.  This is manifested in a mass exodus from platforms like Twitter/X, a ratings collapse for MSNBC,  and even celebrities relocating abroad.  The article highlights examples like Alyssa Milano leaving X, MSNBC's declining viewership, and wealthy individuals seeking escape through luxury travel packages to avoid the Trump administration.  The author satirically frames this behavior as a \"great escape,\" mocking the left's response to the election outcome.
'''

print(requests.post("http://127.0.0.1:8002/analyze_bias",
            json={"text":text}).json)

# # testing purpose
# from summarizer_google import summarize_text, analyze_sentiment
# import asyncio

# async def test_services():
#     # print(await summarize_text("This is a test text for summarization."))
#     print(analyze_sentiment("This is a test text for sentiment analysis."))

# asyncio.run(test_services())