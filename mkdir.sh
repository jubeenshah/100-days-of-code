for i in $(seq 1 100); 
do 
cd "Day-"$i;
rm README.md;
touch README.md
echo "# DAY-"$i>>README.md
cd ..;
done