import os

pages = []

with open("../raw-files/porn_pages.txt", 'r') as f_in:
    for line in f_in.readlines():
        pages.append(line)
    f_in.close()

pages.sort()
pages = list(dict.fromkeys(pages))

try:
    os.remove("../blocklists/block_porn.list")
except OSError:
    pass

with open("../blocklists/block_porn.list", 'a') as f_out:
    f_out.write(
        "# Hostfile\n"
        "#\n"
        "# Author: Evil List\n"
        "#\n"
        "# Fetch the latest version of this file:https://raw.githubusercontent.com/EvilList/my-pihole-blocklist/main/blocklists/block_porn.list\n"
        "# ====================================================================================================================================\n\n"
    )

    for entry in pages:
        f_out.write(f'0.0.0.0 {entry}')
        f_out.write(f'0.0.0.0 www.{entry}')

    f_out.write('\n')

    with open("../raw-files/porn_pages_complex.txt", 'r') as f_in:
        for line in f_in.readlines():
            f_out.write(line)
        f_in.close()