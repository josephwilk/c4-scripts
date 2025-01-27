gather:
	python expired_domains.py

join:
	mkdir -p out/joined/
	cat ./out/*.json > out/joined/all.json
	sort -o out/joined/all_sorted.json out/joined/all.json

filter: 
	grep -ir "disability" out/joined/all.json
