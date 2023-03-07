import re
import argparse


parser = argparse.ArgumentParser(description='Markdown TOC automated generation')
parser.add_argument('--input_path', '-i', 
                    type=str, 
                    required=True,
                    help='the markdown input file path')

parser.add_argument('--output_path', '-o', 
                    type=str, 
                    required=False,
                    help='the output markdown file path')

parser.add_argument('--update_md', '-u',
                    action='store_const',
                    const=True, 
                    default=False, 
                    required=False,
                    help='if used, updates the original markdown file')

parser.add_argument('--output_screen', '-p',
                    action='store_const', 
                    const=True, 
                    default=False, 
                    required=False,
                    help='if used, outputs the TOC on the terminal')

parser.add_argument('--encoding', '-e', 
                    type=str, 
                    default='utf-8', 
                    required=False,
                    help='encoding to be used for read and write files')

parser.add_argument('--toc_header', 
                    type=str, 
                    default='# Table of Contents', 
                    required=False,
                    help='header to be displayed on the TOC')

args = parser.parse_args()
HEADINGS_REGEX = r'^(#+)\s+(.*)$'


def read_file(input_path, encoding):
    with open(file=input_path, mode='r', encoding=encoding) as f:
        text = f.read()
    return text


def write_file(output_path, content, encoding):
    with open(file=output_path, mode='w', encoding=encoding) as f:
        f.write(content)


def build_toc(headings):
    toc = f'{args.toc_header}\n'
    for level, heading in headings:
        identation = '  '*(len(level)-1) + '-'
        
        heading_index = heading.lower()
        heading_index = heading_index.replace(' ', '-') \
                                     .replace('.', '') \
                                     .replace(',', '') \
                                     .replace(':', '') \
                                     .replace(';', '') \
                                     .replace('!', '') \
                                     .replace('?', '')
        
        toc += f'{identation} [{heading}](#{heading_index})\n'
    return toc


if __name__ == '__main__':
    print(args)

    text = read_file(args.input_path, args.encoding)
    headings = re.findall(HEADINGS_REGEX, text, flags=re.MULTILINE)
    toc = build_toc(headings)

    output_options = {
        args.output_path: {
            'output_path': args.output_path,
            'content': toc, 
            'encoding': args.encoding
        },
        args.update_md: {
            'output_path': args.input_path,
            'content': toc+'\n'+text, 
            'encoding': args.encoding
        }
    }
    
    if args.output_path:
        write_file(**output_options.get(args.output_path))

    if args.update_md:
        write_file(**output_options.get(args.update_md))
    
    if args.output_screen:
        print('\n' + toc)
