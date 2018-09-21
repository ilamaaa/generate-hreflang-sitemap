# simple enough feed it a mapping file with the comma sperated format
# hreflang code, hreflang code, hreflang code
# coresponding url, corresponding url, corresponging url
# coresponding url1, corresponding url1, corresponging url1


def get_data(file):
    with open(file) as f:
        data = f.read()
        return data

def get_unique_links(data):
    lines = data.split("\n")
    urls = []
    for line in lines:
        if line == lines[0]:
            pass
        else:
            urls = urls + line.split(",")
    unique_urls = list(set(urls))
    return unique_urls

def get_codes(data):
    lines = data.split("\n")
    langs = lines[0].split(",")
    return langs

def gen_url_element(url,data,codes):
    element_currently = """<url><loc>""" + url + """</loc>"""
    for line in data.split("\n"):
        row = line.split(",")
        if url in row:
            for code in codes:
                link = row[codes.index(code)]
                if link == "x":
                    pass
                else:
                    element_currently = element_currently + """<xhtml:link rel="alternate" hreflang='""" + code + """' href='""" + link + """'/>"""
    return element_currently


def main(file):
    sitemap_cur = """<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n"""
    data = get_data(file)
    urls = get_unique_links(data)
    codes = get_codes(data)
    for url in urls:
        sitemap_cur = sitemap_cur + gen_url_element(url, data, codes) + "\n"
    return sitemap_cur + """</urlset>"""

print(main("pages.txt"))

