import os
import sys
import getopt

options = ["porn", "ads"]

io_files = {
    "porn": ["../raw-files/porn_pages.txt", "../blocklists/block_porn.list", "../raw-files/porn_pages_complex.txt"],
    "ads": ["../raw-files/ad_pages.txt", "../blocklists/block_adpages.list", "../raw-files/ad_pages_complex.txt"]
}

def parseArgs(argv):
    try:
        opts, args = getopt.getopt(argv, "ho:", ["option="])
    except getopt.GetoptError:
        print('usage: create_hostfiles.py -o <option>')
        sys.exit(2)
    
    if not opts:
        print('usage: create_hostfiles.py -o <option>')
        sys.exit()
    else:
        for opt, arg in opts:
            if opt == '-h':
                print('usage: create_hostfiles.py -o <option>')
                sys.exit()
            elif opt in ("-o", "--option"):
                return arg


def createHostfile(io_list):
    input = io_list[0]
    output = io_list[1]
    additional = io_list[2]

    pages = []

    with open(input, 'r') as f_in:
        for line in f_in.readlines():
            pages.append(line)
        f_in.close()

    pages.sort()
    pages = list(dict.fromkeys(pages))

    try:
        os.remove(output)
    except OSError:
        pass

    with open(output, 'a') as f_out:
        f_out.write(
            "# Hostfile\n"
            "#\n"
            "# Author: Evil List\n"
            "# ===========================\n\n"
        )

        for entry in pages:
            f_out.write(f'0.0.0.0 {entry}')
            f_out.write(f'0.0.0.0 www.{entry}')

        f_out.write('\n')

        with open(additional, 'r') as f_in:
            for line in f_in.readlines():
                f_out.write(line)
            f_in.close()


def main(argv):
    option = parseArgs(argv)
    
    if option in options:
        createHostfile(io_files.get(option))
    elif option == "all":
        for op in options:
            createHostfile(io_files.get(op))
    else:
        print("Invalid option! Available options are:\n  porn  ads  all")


if __name__ == "__main__":
   main(sys.argv[1:])