# Acompanhamento dos jogos da Mega Sena

```sh
mamba env create
conda activate megasena
pip-sync requirements-dev.txt
pre-commit install

# After update `setup.cfg`
pip-compile setup.cfg --resolver backtracking -o requirements.txt
pip-compile setup.cfg --resolver backtracking -o requirements-dev.txt --extra dev
```

## Run
```sh
python -m streamlit run src/demo.py
```
