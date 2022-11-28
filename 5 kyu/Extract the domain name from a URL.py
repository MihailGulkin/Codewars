def domain_name(url):
    if '//' in url:
        url = url[url.find('//') + 2:]
    url = url.replace('www.', '')
    url = url[:url.find('.')]
    return url
