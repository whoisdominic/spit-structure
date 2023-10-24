#!/usr/bin/env python3

import os
import argparse

# Default ignored directories and files
default_ignored = {
    "node_modules",
    ".git",
    ".yarn",
    "Pods",
    "Build",
    ".vscode",
    ".gradle",
    "DerivedData"
}

def print_directory_structure(path, depth=None, ignored=None, indent=0):
    """Recursively prints the directory structure."""
    # If depth is zero, we won't proceed
    if depth == 0:
        return
    
    # Check if the directory or file is in the ignored list
    if os.path.basename(path) in ignored:
        return

    # Base case: If path is a file, print its name
    if os.path.isfile(path):
        print('  ' * indent + '- ' + os.path.basename(path))
        return

    # If path is a directory, print its name and then its contents
    print('  ' * indent + '- /' + os.path.basename(path))
    for item in sorted(os.listdir(path)):
        # If depth is not None, decrement it for the next level
        next_depth = depth - 1 if depth is not None else None
        print_directory_structure(os.path.join(path, item), next_depth, ignored, indent + 1)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Print directory structure.")
    parser.add_argument('-depth', '-d', type=int, default=None, help="Max depth to traverse. Default is infinite depth.")
    parser.add_argument('-ignore', '-i', nargs='*', default=[], help="Names of additional directories or files to ignore.")
    args = parser.parse_args()

    # Add user-specified ignored items to the default set
    ignored = default_ignored.union(args.ignore)

    # Call the function with the specified depth and ignored set
    print_directory_structure(os.getcwd(), args.depth, ignored)

if __name__ == "__main__":
    main()
