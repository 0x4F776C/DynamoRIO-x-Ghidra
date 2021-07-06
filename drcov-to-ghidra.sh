#!/bin/sh

Help() {
  echo "[Description]"
  echo "Convert drcov text log for use in Ghidra API"
  echo
  echo "[Usage]"
  echo "$0 drcov.log 0x000 0x004"
  echo
  echo "[Explanation]"
  echo "drcov.log       drcov text log file"
  echo "0x000           drcov offset"
  echo "0x004           Binary offset"
  echo
}

while getopts ":h" option;
do
        case $option in
                h)
                        Help
                        exit;;
        esac
done

if [ -z $1 ] || [ -z $2 ] || [ -z $3 ]
then
        Help
        exit 1
else
        grep "module\[  0\]" $1 |
        awk -F' ' '{print substr($3, 1, length($3)-1)}' |
        # sed -e 's/.*/"&",/' |
        sed "s/$2/$3/g" > BBs.txt
fi
