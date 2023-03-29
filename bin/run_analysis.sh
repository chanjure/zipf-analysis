mkdir data
curl -L -o data/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt

mkdir results
for book in dracula frankenstein
do
  python bin/countwords.py data/${book}.txt --num 100 > results/${book}.csv
  python bin/plotcounts.py results/${book}.csv results/${book}.pdf --xlim 0 3000
done
