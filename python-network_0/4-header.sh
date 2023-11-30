#!/bin/bash
# 4-header.sh

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
header="X-HolbertonSchool-User-Id: 98"

curl -sH "$header" "$url"
