gather:
	python expired_domains.py

join:
	mkdir out/joined/
	cat ./out/*.json > out/joined/all.json
