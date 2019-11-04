from lib import filesplitter
from argparse import ArgumentParser

def splitter_args():
    parser = ArgumentParser(description="File Splitter")
    parser.add_argument('-s','--split', action='store_true', dest='split', default=True)
    parser.add_argument('-r','--recursive', action='store_true', dest='recurse', default=False)
    parser.add_argument('-x','--delete', action='store_true', dest='delete', default=False)
    parser.add_argument('-f','--file', action='store', dest='filename')
    parser.add_argument('-o','--output', action='store', dest='outputs')
    parser.add_argument('-l','--lines', action='store', dest='linesize')
    parser.add_argument('-t','--toplevel', action='store', dest='rootdir')
    args = parser.parse_args()
    return args

def s_parser():
    args = splitter_args()
    splitfile = filesplitter.split()
    if args.split == True:
        if args.filename and args.outputs and args.linesize and not args.recurse:
            splitfile.filesplitter(args.linesize,args.filename,args.outputs)
            #if args.delete == True:
            #    splitfile.removebasefile(filename)
        elif args.recurse == True and not args.filename:
            if args.linesize and args.rootdir and args.outputs:
                splitfile.recursivesplitter(args.linesize,args.rootdir,args.outputs)
                #if args.delete == True:
                #    splitfile.removebasefile(filename)
                # CAREFUL !
            else:
                print("Expected --lines --toplevel --output")
        else:
            print("-h or --help for help")
    else:
        print("-h or --help for help")
        exit(1)

if __name__ == '__main__':
    s_parser()
            
    
