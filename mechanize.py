import mechanize

def make_browser():
    """
    A function to make browser object.
    """
    browser = mechanize.make_browser()

    # Making Cookie Jar and bind it to browser
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)

    # Setting browser options
    browser.set_handle_equiv(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),
                               max_time=1)

    browser.addheaders = [('User-agent',
                          ('Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3)'
                           ' Gecko/20041001 Firefox/0.10.1'))]
    return browser


if __name__ == '__main__':
    browser = make_browser()

    browser.open('http://apps.who.int/trialsearch/Default.aspx')
