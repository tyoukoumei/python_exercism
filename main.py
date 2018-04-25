import sys
from pathlib import Path


def main(file_name: str, md: str, target: str, expectation: str):
    import nbformat as nbf
    nb = nbf.v4.new_notebook()
    nb['cells'] = [nbf.v4.new_markdown_cell(md),
                   nbf.v4.new_code_cell(target),
                   nbf.v4.new_code_cell(expectation)]

    dest = Path("./notebooks")
    dest = dest.joinpath(file_name)
    with open(dest, 'w') as dest:
        nbf.write(nb, dest)


def get_class_index(lines: list):
    for index, line in enumerate(lines):
        if line.startswith("class"):
            return index
    raise Exception("Bad Format")


def normalize(original: str, module_name: str):
    file_content = []

    body = original.splitlines()
    idx = get_class_index(body)

    header = body[0:idx]
    rest = body[idx:]

    pkg = ""
    module_name = module_name.replace("-", "_")

    for line in header:
        if line.startswith("from " + module_name):
            pass
        elif line.startswith("import " + module_name):
            pkg = module_name
        else:
            file_content.append(line)

    for line in rest:
        if line.startswith("if __name__ == '__main__':"):
            break
        else:
            if pkg != "":
                file_content.append(line.replace(pkg + ".", ""))
            else:
                file_content.append(line)
    file_content.append("unittest.main(argv=[''], exit=False)")
    file_content.append("")
    return '\n'.join(file_content)


def generate_exercism(d: str, seq=None):
    p = Path(d)
    if seq:
        f_name = "{:03d}_{}.ipynb".format(seq, p.name)
    else:
        f_name = p.name
    for f in p.glob('**/*'):
        # print(str(f))
        if not f.is_dir():
            with open(f) as fd:
                content = fd.read()
            if str(f).endswith("test.py"):
                exp = content
            elif str(f).endswith("py"):
                src = content
            elif str(f).endswith("/README.md"):
                doc = content
            else:
                print("Unexpected: ", str(f))
    exp = normalize(exp, p.name)
    main(f_name, doc, src, exp)


def loop_parent(d: str):
    with open("./order.txt") as order:
        for i, l in enumerate(order):
            p = Path(d)
            generate_exercism(p.joinpath(l.strip()), i)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("no folder is specified.")
    else:
        d = sys.argv[1]
        if d == "python":
            loop_parent(d)
        else:
            print("unexpectd")
