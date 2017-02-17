import os 
import argparse



def traverse(directory, depth=0):
    if os.path.isdir(directory):
        items = os.listdir(directory)
        for item in items:
            print "-"*(depth+3) + item
            fullpath = os.path.join(directory, item)
            if os.path.isdir(fullpath):
                traverse(fullpath, depth+3)
            
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="this program traverse \
    directories and prints the file listing in a hierarchical way")
    parser.add_argument("-d", "--dir", required=True, help="Directory to traverse")
    args = parser.parse_args()
    traverse(args.dir)