from lib import parse
from argparse import ArgumentParser

def parser_args():
    parser = ArgumentParser(description="Credential parser")
    parser.add_argument('-p','--parse', action='store_true', dest='parse', default=True)
    parser.add_argument('-f','--file', action='store', dest='filename')
    parser.add_argument('-d','--delimiter', action='store', dest='delimiter')
    parser.add_argument('-s','--size', action='store_true', dest='size', default=False)
    parser.add_argument('-r','--recursive', action='store_true', dest='recurse', default=False)
    parser.add_argument('-t','--toplevel', action='store', dest='rootdir')
    args = parser.parse_args()
    return args

def p_parser():
    args = parser_args()
    parsecreds = parse.parser()
    if args.parse == True:
        if args.filename and args.delimiter and not args.recurse:
            creds = parsecreds.extract_creds(args.filename,args.delimiter)
            print(creds)
            if args.size == True:
                print("%s credentials in array" % str(parsecreds.credsize()))
            parsecreds.cleanup()
        elif args.recurse == True and not args.filename:
            if args.rootdir and args.delimiter:
                creds = parsecreds.recursive_extract(args.rootdir,args.delimiter)
                print(creds)
                if args.size == True:
                    print("%s credentials in array" % str(parsecreds.credsize()))
            else:
                print("Expected --toplevel and --delimiter")
                if args.size == True:
                    print("%s credentials in array" % str(parsecreds.credsize()))
        else:
            print("-h or --help or help")

    else:
        print("-h or --help for help")
        exit(1)

if __name__ == '__main__':
    p_parser()
