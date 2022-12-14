import sys

file = sys.argv[1]

def wordcount(file):
    import json
    import re
    with open(file, encoding='utf-8') as json_file:
        data = json.load(json_file)
    char_count = 0
    for each in data['cells']:
        if not each['metadata']:  # if there is no metadata
            continue
        cell_type = each['cell_type']
        tags = each['metadata']['tags']
        if cell_type == "markdown" and 'countthis' in tags:
            content = each['source']
            for line in content:
                temp = line.replace("\n", "").replace(" ", "")  # remove all spaces and newlines from a string
                temp = re.sub("[\(\[].*?[\)\]]", "", temp)  # remove footnotes, e.g., [^footnote]
                char_count = char_count + len(temp)
    print('Anzahl an Zeichen: ' + str(char_count) + ' (exklusive Leerzeichen und Fußnoten)')

wordcount(file=file)
