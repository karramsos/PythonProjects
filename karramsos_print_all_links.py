#! /usr/bin/python
# author Sukhvinder Singh | karramsos@gmail.com | @karramsos
# a small code snippet to print all links on a webpage

def get_next_target(page):
    start_link = page.find('<a href=')
    
    if start_link ==-1:
        url, end_quote = None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

#insert yout url here
print_all_links(get_page('www.xxx.com'))