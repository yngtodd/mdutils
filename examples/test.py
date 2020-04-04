from pathlib import Path
from mdutils.mdutils import MdUtils


mdFile = MdUtils(file_name=f"{Path('Example')}",title='This is a Markdown File Example')
mdFile.create_md_file()
mdFile.new_header(level=1, title='Atx Header 1')
mdFile.new_line()
mdFile.new_image('results', './history.png')
mdFile.new_line()
mdFile.new_header(level=2, title='Sub header')
mdFile.create_md_file()

print(mdFile.file_data_text)
