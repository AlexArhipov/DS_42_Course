tail -n +2 ../ex01/hh.csv > hh_sorted_temp.csv
head -n 1 ../ex01/hh.csv > hh_sorted.csv
sort --field-separator="," -k2 -k4 hh_sorted_temp.csv  >> hh_sorted.csv 