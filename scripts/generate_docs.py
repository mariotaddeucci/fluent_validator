import ast
import glob
import os


def extract_validators_docs(filename):
    with open(filename, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            if docstring:
                docstring = [
                    line.strip() for line in docstring.split("\n") if line.strip() != ""
                ]
                docstring = "\n".join(docstring)

                method_name = node.name.strip("_")
                args = [arg.arg for arg in node.args.args if arg.arg != "self"]
                yield f"**{method_name}({', '.join(args)})** {docstring}"


def main():
    project_dir = os.path.join(os.path.dirname(__file__), "..")
    validators_dir = os.path.join(project_dir, "fluent_validator", "validators")
    output_file = os.path.join(project_dir, "validators.md")

    with open(output_file, "w", encoding="utf-8") as out:
        for file in glob.glob(os.path.join(validators_dir, "*.py")):
            for validator_doc in extract_validators_docs(file):
                out.write(f"{validator_doc}\n")


if __name__ == "__main__":
    main()
