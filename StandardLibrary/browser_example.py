import webbrowser


search_term = input("Enter a search term: ")
print(webbrowser.open(f"https://google.com/search?q={search_term}"))
