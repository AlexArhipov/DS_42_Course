awk -F ',' ' {print $5} '  OFS="," ../ex03/hh_positions.csv > count_temp.csv
awk -F ',' '{gsub("-","",$1); print}' OFS="," count_temp.csv > hh_sorted1.csv
awk '!freq[$1]++{order[++k]=$1} END{for (i=1; i<=k; i++) print order[i], "(" freq[order[i]] ")"}' hh_sorted1.csv > count_temp.csv
tail -n +2 count_temp.csv > temp.text
rm hh_sorted1.csv
rm count_temp.csv
echo "name, count" > hh_uniq_positions.csv
sed 's/[ \t]/,/g' temp.text >> hh_uniq_positions.csv
rm temp.text