from pathlib import Path
import re
import argparse
from .process import process


def configure():
    parser = argparse.ArgumentParser(description='Japanese Wikipedia cleaner')
    parser.add_argument('-i', '--input', help='input file path', type=str)
    parser.add_argument('-o', '--output', help="output file path", type=str)

    args = parser.parse_args()    # 4. 引数を解析

    if args.input is None:
        raise ValueError("\nPlease specify input file path!")
    elif args.output is None:
        input_dir, input_filename = "/".join(
            args.input.split("/")[:-1]), args.input.split("/")[-1]
        args.output = f"{input_dir}/cleaned-{input_filename}"

    return args


def main():
    args = configure()
    INPUT, OUTPUT = Path(args.input), Path(args.output)

    if not INPUT.exists():
        raise ValueError(f"{INPUT} is not exists.")

    with INPUT.open() as f, OUTPUT.open("w") as w:
        prev_is_newline = False
        for line in f:
            if "(曖昧さ回避)" in line:
                while "</doc>" != line:
                    line = next(f).strip()
                continue

            if re.match(r'<doc.*>', line.strip()):
                try:
                    _ = next(f)
                    _ = next(f)
                    line = next(f)
                except:
                    continue

            if line.strip() == "</doc>":  # 閉じタグを無視
                if not prev_is_newline:
                    w.write("\n")
                prev_is_newline = True
                continue

            if re.match(r'.*。$', line.strip()) is None:  # 。で終わっていなければ無視
                continue

            if re.match(r'\[\[File', line.strip()):  # wiki リンクを無視
                continue

            else:
                text = process(line)
                if len(text) <= 10:
                    continue
                if text:
                    prev_is_newline = False
                    w.write(text + "\n")


if __name__ == "__main__":
    main()
