import yaml
import re
import sys
import shutil
import argparse


def insert_tag(file):
    m = re.compile(r"#\w*")

    replace_str = ""
    not_need = False

    with open(file, "r") as f:
        for line in f:
            if line.startswith("Type::"):
                l = m.findall(line)
                l = [s.replace("#", "") for s in l]
                if l:
                    replace_str = yaml.dump({"tags": l})
            if line.startswith("tags:"):
                not_need = True

    if not replace_str:
        print(f"Failed to find pattern in {file}")
        return

    if not_need:
        print(f"Tag already replaced in {file}")
        return

    count_rule = 0
    done_insert = False
    with open(file, "r") as read_file:
        with open(f"{file}.tmp", "w") as write_file:
            for line in read_file:
                if line.strip() == "---":
                    count_rule += 1
                if count_rule == 2 and not done_insert:
                    done_insert = True
                    write_file.write(replace_str)
                write_file.write(line)

    shutil.move(f"{file}.tmp", file)
    print(f"Success on {file}")


def insert_link(file):
    m = re.compile(r"\[[^\]]*\]\]")

    replace_str = ""
    not_need = False

    with open(file, "r") as f:
        for line in f:
            if line.startswith("Tags::"):
                l = m.findall(line)
                if l:
                    replace_str = yaml.dump({"link": l})
            if line.startswith("link:"):
                not_need = True

    if not replace_str:
        print(f"Failed to find pattern in {file}")
        return

    if not_need:
        print(f"Link already replaced in {file}")
        return

    count_rule = 0
    done_insert = False
    with open(file, "r") as read_file:
        with open(f"{file}.tmp", "w") as write_file:
            for line in read_file:
                if line.strip() == "---":
                    count_rule += 1
                if count_rule == 2 and not done_insert:
                    done_insert = True
                    write_file.write(replace_str)
                write_file.write(line)

    shutil.move(f"{file}.tmp", file)
    print(f"Success on {file}")


def clean_up(file):
    filter_substr = [
        "Tags:",
        "Type:",
        "Last Updated:",
        "Originally published:",
        "Author:",
    ]
    with open(file, "r") as read_file:
        with open(f"{file}.tmp", "w") as write_file:
            for line in read_file:
                found = False
                for s in filter_substr:
                    if s in line:
                        found = True
                if found:
                    continue
                write_file.write(line)

    shutil.move(f"{file}.tmp", file)
    print(f"Success on {file}")


def main():
    f = " ".join(sys.argv[1:])
    print(f)
    if f.endswith(".md"):
        clean_up(f)
        # insert_link(f)
        # insert_tag(f)


if __name__ == "__main__":
    main()
