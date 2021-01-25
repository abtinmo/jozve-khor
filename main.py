from tika import parser

import re
import os
import sys


def remove_tags(text):
    tag_re = re.compile(r"<[^>]+>")
    return tag_re.sub("", text)


def parse_file(file_path, text):
    parsed_pdf = parser.from_file(file_path, xmlContent=True)
    data = parsed_pdf['content']
    for page_number, page in enumerate(data.split('<div class="page">')):
        if text in page:
            print(f"text was found in file: {file_path}, page: {page_number}\n\n")
            print(remove_tags(page))


if __name__ == "__main__":
    _, file_path, text_to_serch_for = sys.argv

    if os.path.isdir(file_path):
        directory_path = file_path
        # todo parse all pdf files
        for file_path in os.listdir(directory_path):
            if file_path.endswith(".pdf"):
                parse_file(file_path, text_to_serch_for)

    elif os.path.isfile(file_path):
        parse_file(file_path, text_to_serch_for)