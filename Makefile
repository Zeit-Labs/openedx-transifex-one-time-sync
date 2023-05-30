transifex_langs = "ar,fr_CA,de"

sync:
	python 3-create-tx-config-files.py
	cd download && tx pull -f --mode=reviewed -l $(transifex_langs)
