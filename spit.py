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
    ".Trash",
    ".DS_Store",
}


def print_directory_structure(path, depth=None, ignored=None, verbose=False, show_hidden=False, indent="", last=True):
    """Recursively prints the directory structure."""

    # Adds a prefix to the current file or directory
    prefix = "└─ " if last else "├─ "
    # Adds padding to the current file or directory
    padding = "    " if last else "│  "

    # If depth is zero, we won't proceed
    if depth == 0:
        return

    # Check if the directory or file is in the ignored list
    if not verbose and os.path.basename(path) in ignored:
        return

    # Print current file or directory
    print(indent + prefix + os.path.basename(path))

    # If path is a directory, print its contents
    if os.path.isdir(path):
        items = sorted([item for item in os.listdir(path) if (
            show_hidden or not item.startswith('.')) and item not in ignored])
        for index, item in enumerate(items):
            next_depth = depth - 1 if depth is not None else None
            print_directory_structure(
                os.path.join(path, item),
                next_depth,
                ignored,
                verbose,
                show_hidden,
                indent + padding,
                index == len(items) - 1
            )


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Print directory structure.")
    parser.add_argument('-depth', '-d', type=int, default=None,
                        help="Max depth to traverse. Default is infinite depth.")
    parser.add_argument('-verbose', '-v', action='store_true',
                        help="Verbose mode. Ignores all default ignored directories and files.")
    parser.add_argument('-ignore', '-i', nargs='*', default=[],
                        help="Names of additional directories or files to ignore.")
    parser.add_argument('-a', action='store_true', help="Show hidden files.")

    # Parse arguments
    args = parser.parse_args()

    # Add user-specified ignored items to the default set
    ignored = default_ignored.union(args.ignore)

    # Call the function with the specified depth, hidden and ignored set
    print_directory_structure(os.getcwd(), args.depth,
                              ignored, args.verbose, args.a)


if __name__ == "__main__":
    main()
