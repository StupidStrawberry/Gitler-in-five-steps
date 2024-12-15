import wikipedia

wikipedia.set_lang("ru")
name_of_page = wikipedia.random(pages=1)
print(name_of_page)


def step(page_name, turn):
    global page
    try:
        page = wikipedia.page(page_name)
    except wikipedia.exceptions.DisambiguationError:
        return None
    except wikipedia.exceptions.PageError:
        return None
    finally:
        links = list(page.links)
        print(page_name, turn)
        if 'Гитлер, Адольф' in page.links and turn + 1 <= 5:
            return page_name + "; " + 'Гитлер, Адольф'
        elif turn < 4 and page_name[0] != r"\d":
            for link in links:
                x = step(link, turn + 1)
                if x != None:
                    return page_name + "; " + x
        else:
            return None


print(step(name_of_page, 0))
