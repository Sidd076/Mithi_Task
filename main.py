import re
from collections import defaultdict

class WordIndexer:
    def __init__(self):
        self.word_index = defaultdict(set)

    def process_pages(self, pages, exclude_words):
        for page_number, content in pages:
            words = re.findall(r'\b\w+\b', content.lower())
            for word in words:
                if word not in exclude_words:
                    self.word_index[word].add(page_number)

    def write_index_to_file(self, output_file_path):
        with open(output_file_path, 'w') as f:
            for word in sorted(self.word_index.keys()):
                page_numbers = sorted(self.word_index[word])
                f.write(f"{word} : {', '.join(map(str, page_numbers))}\n")

def read_pages_from_files(file_paths):
    pages = []
    for i, file_path in enumerate(file_paths, 1):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            pages.append((i, content))
    return pages

def read_exclude_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        exclude_words = set(f.read().split())
    return exclude_words

def main():
    page_files = ["Page1.txt", "Page2.txt", "Page3.txt"]
    pages = read_pages_from_files(page_files)

    exclude_words = read_exclude_words("exclude-words.txt")

    indexer = WordIndexer()
    indexer.process_pages(pages, exclude_words)
    indexer.write_index_to_file("index.txt")

if __name__ == "__main__":
    main()
