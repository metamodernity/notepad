import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Это текст после функции")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://itproger.com")
