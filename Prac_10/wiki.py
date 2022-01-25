import wikipedia

user_input = input("What do you want to search? ")
while user_input != "":
    try:
        page = wikipedia.page(user_input, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
    except wikipedia.DisambiguationError as e:
        print(e.options)
        user_input = input("What do you want to search? ")