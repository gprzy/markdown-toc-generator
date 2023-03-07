# Markdown Table of Contents (TOC) Generator
📌 A simple Markdown Table of Contents (TOC) generator

## Usage example
To run the example, go to `src` and run:

```bash
python3 markdown_toc_generator.py -i '../examples/example.md' -o '../examples/example_toc.md' -u -p
```

Where:
- `-i`: the input Markdown file path;
- `-o`: the output markdown file path to save the TOC;
- `-u`: if passed, will update the original file with the TOC;
- `p`: if passed, will output on terminal the TOC;

This will output the following:

```bash
Namespace(input_path='../examples/example.md', output_path='../examples/example_toc.md', update_md=True, output_screen=True, encoding='utf-8', toc_header='# Table of Contents')

# Table of Contents
- [Chapter 1](#chapter-1)
  - [This is a subheader](#this-is-a-subheader)
  - [And this is another one](#and-this-is-another-one)
- [Chapter 2](#chapter-2)
- [Chapter 3](#chapter-3)
  - [Section 1](#section-1)
    - [Topic 1](#topic-1)
    - [Topic 2](#topic-2)
- [End of the Markdown file!](#end-of-the-markdown-file)
```

The command has read the `example.md` file, generated and updated the same file with the TOC and then saved the TOC in the `example_toc.md` file, finally displaying the TOC on the terminal.

## Usage options
To see the usage options, you can go to `src` and run:

```bash
python3 markdown_toc_generator.py --help
```

This command will display the structure and available arguments:

```powershell
usage: markdown_toc_generator.py [-h] --input_path INPUT_PATH [--output_path OUTPUT_PATH] [--update_md] [--output_screen] [--encoding ENCODING] [--toc_header TOC_HEADER]
```

Options:
- `-h` or `--help`: show this help message and exit;
- `--input_path` or `-i INPUT_PATH`: the markdown input file path;
- `--output_path` or `-o OUTPUT_PATH`: the output markdown file path;
- `--update_md` or `-u`: if used, updates the original markdown file;
- `--output_screen` or `-p`: if used, outputs the TOC on the terminal;
- `--encoding` or `-e ENCODING`: encoding to be used for read and write files;;
- `--toc_header TOC_HEADER`: header to be displayed on the TOC;