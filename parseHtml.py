import re


def parseHtml(rawHtmlString):
    splittedHtmlString = rawHtmlString.splitlines()
    regex = '<p(.*)</p>'

    parsedHtml = []
    for htmlLine in splittedHtmlString:
        match = re.search(regex, htmlLine, re.IGNORECASE)
        if match:
            parsedHtml.append(match.group(1))

    return parsedHtml

    # return list(map(lambda html: re.search(regex, html).group(1), splittedHtmlString))
# print(less_than_zero)


if __name__ == "__main__":
    rawHtmlString = "<p id = \"L93\" > それは、なんと不幸なことか。< /p ><p id = \"L94\" > <br / > < /p >\n<p id = {\"L97\"} > 次々と涙が溢れでてくる。こんな姿を誰にも見せるわけにはいかない。わたくしは音を立てないように気をつけながら、そっと扉の前を離れた。< /p >\n</div >"

    response = parseHtml(rawHtmlString)
    print(response)
