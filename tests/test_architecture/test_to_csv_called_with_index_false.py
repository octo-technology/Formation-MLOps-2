"""Architecture test.

Vérifie que tous les appels à `to_csv` faits dans le package
`formation_mlops_2` sont bien appelés avec l'argument `index=False`.

Cela évite d'écrire l'index du DataFrame dans les fichiers CSV générés
(données, prédictions, etc.).
"""

from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[2] / "formation_mlops_2"



def test_to_csv_called_with_index_false():
    # Given
    assert False # noqa: B011
