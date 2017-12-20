#!/bin/bash

set -x

temp_and_humidity=$(python dht22.py)

file_path=$(raspistill -o "/tmp/pic-%d-$temp_and_humidity.jpg" -ts -q 8 -h 1080 -w 1280 -v 2>&1 | grep "Opening output file " | awk '{ gsub(/Opening output file /, ""); print }')

file=$(echo $file_path | awk '{gsub("/tmp/", ""); print}')

file_size=$(stat --printf="%s" $file_path)

aws s3api put-object --bucket pi-pics --body "$file_path" --key "$file"

echo "Wrote $file_size bytes to S3 key $file"

