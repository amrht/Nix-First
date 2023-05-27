import sys
sys.path.append('result/lib/python3.9/site-packages')
import wikipedia

while True:
    search_query = input("Enter a search query (or 'q' to quit): ")

    if search_query.lower() == 'q':
        break

    try:
        page = wikipedia.page(search_query)
        print("\nTitle:", page.title)
        print("\nSummary:", page.summary)
        print("\nURL:", page.url)
        print("\n\nCategories:", page.categories)
        print("")

    except wikipedia.DisambiguationError as e:
        print(f"DisambiguationError: '{search_query}' may refer to multiple pages. Please provide a more specific query.")
        print("Options:")
        for option in e.options:
            print("-", option)
        print("")

    except wikipedia.PageError:
        try:
            page = wikipedia.page(search_query, auto_suggest=False)
            print("\nTitle:", page.title)
            print("\nSummary:", page.summary)
            print("\nURL:", page.url)
            print("\n\nCategories:", page.categories)
            print("")

        except wikipedia.PageError:
            print(f"PageError: '{search_query}' does not exist on Wikipedia.")
            print("")

print("\nExiting...")

