pages = []

with open("../raw-files/porn_pages.txt", 'r') as f_in:
    for line in f_in.readlines():
        pages.append(line)

pages.sort()
pages = list(dict.fromkeys(pages))

with open("../raw-files/porn_pages_ordered.txt", 'a') as f_out:
    for entry in pages:
        f_out.write(f'{entry}')