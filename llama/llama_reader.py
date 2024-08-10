from llama_index.readers.file.flat_reader import FlatReader
from pathlib import Path

reader = FlatReader()
docs_2021 = reader.load_data(Path("tesla_2021_10k.htm"))
docs_2020 = reader.load_data(Path("tesla_2020_10k.htm"))
