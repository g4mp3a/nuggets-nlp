from textblob import TextBlob
import wikipedia


def search_wikipedia(name: str):
    """ "Search Wikipedia"""
    print(f"Searching for {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name: str):
    """Summarize Wikipedia"""
    print(f"Wikipedia summary for {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Returns a `TextBlob` object"""
    return TextBlob(text)


def get_phrases(name: str):
    """Find noun phrases from wikipedia"""
    summary_text = summarize_wikipedia(name)
    blob = get_text_blob(summary_text)
    return blob.noun_phrases
