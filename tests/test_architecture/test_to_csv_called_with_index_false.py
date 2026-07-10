"""Architecture test.

Vérifie que tous les appels à `to_csv` faits dans le package
`formation_mlops_2` sont bien appelés avec l'argument `index=False`.

Cela évite d'écrire l'index du DataFrame dans les fichiers CSV générés
(données, prédictions, etc.).
"""

import ast
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[2] / "formation_mlops_2"


def _iter_python_files(root: Path):
    yield from root.rglob("*.py")


def _iter_to_csv_calls(tree: ast.AST):
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "to_csv"
        ):
            yield node


def _has_index_false(call: ast.Call) -> bool:
    for keyword in call.keywords:
        if keyword.arg == "index":
            return isinstance(keyword.value, ast.Constant) and keyword.value.value is False
    return False


def test_to_csv_called_with_index_false():
    # Given
    violations = []

    for file_path in _iter_python_files(PACKAGE_ROOT):
        source = file_path.read_text()
        tree = ast.parse(source, filename=str(file_path))

        # When
        for call in _iter_to_csv_calls(tree):
            if not _has_index_false(call):
                violations.append(f"{file_path.relative_to(PACKAGE_ROOT.parent)}:{call.lineno}")

    # Then
    assert not violations, (
        "Les appels à to_csv suivants ne sont pas faits avec index=False: "
        f"{', '.join(violations)}"
    )
