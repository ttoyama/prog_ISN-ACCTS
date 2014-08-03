import httplib2
h = httplib2.Http(".cache")
resp, content = h.request("http://apps.who.int/trialsearch/Default.aspx", "GET")
content

