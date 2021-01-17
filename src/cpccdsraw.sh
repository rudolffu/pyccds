#! /bin/bash
for name in fym*fits
do
    newname="$(echo "$name" | sed 's/fym//')"
    cp "$name" "$newname"
done
if [ ! -d "./raw" ]; then
  mkdir ./raw
fi
mv fym*fits ./raw/
