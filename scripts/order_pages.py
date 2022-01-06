import sys
import getopt

options = ["porn", "ads"]

io_files = {
    "porn": ["../raw-files/porn_pages.txt", "../raw-files/porn_pages_ordered.txt"],
    "ads": ["../raw-files/ad_pages.txt", "../raw-files/ad_pages_ordered.txt"]
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

def sortPages(io_list):
    input = io_list[0]
    output = io_list[1]

    pages = []

    with open(input, 'r') as f_in:
        for line in f_in.readlines():
            pages.append(line)

    pages.sort()
    pages = list(dict.fromkeys(pages))

    with open(output, 'a') as f_out:
        for entry in pages:
            f_out.write(f'{entry}')

def main(argv):
    option = parseArgs(argv)
    
    if option in options:
        sortPages(io_files.get(option))
    elif option == "all":
        for op in options:
            sortPages(io_files.get(op))
    else:
        print("Invalid option! Available options are:\n  porn  ads  all")


if __name__ == "__main__":
   main(sys.argv[1:])