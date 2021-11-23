awk -F ',' '{gsub("Junior","1",$5); print}' OFS="," ../ex02/hh_sorted.csv > hh_sorted1.csv
awk -F ',' '{gsub("Middle","2",$5); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
awk -F ',' '{gsub("Senior","3",$5); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
awk ' {print $1,$2,$3,$4,$5} ' hh_sorted1.csv > hh_sorted2.csv
awk -F ',' '{gsub(/([^0-9][^0-9]*)/,"",$5); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
awk -F ',' '{gsub("","-",$5); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
awk -F ',' '{gsub("-1-","Junior",$5); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
awk -F ',' '{gsub("-2-","Middle",$5); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
awk -F ',' '{gsub("-3-","Senior",$5); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
awk -F ',' '{gsub("1-","/Junior",$5); print}' OFS="," hh_sorted1.csv > hh_sorted2.csv
awk -F ',' '{gsub("2-","/Middle",$5); print}' OFS="," hh_sorted2.csv > hh_sorted1.csv
awk -F ',' '{gsub("3-","/Senior",$5); print}' OFS="," hh_sorted1.csv > hh_positions.csv
rm hh_sorted2.csv hh_sorted1.csv