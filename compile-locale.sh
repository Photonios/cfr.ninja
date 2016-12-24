#!/bin/bash

for po_file in locale/*.po; do
    language="${po_file%.*}"
    dir="$language/LC_MESSAGES"

    mkdir -p "$dir"
    cp "$po_file" "$dir"
    msgfmt -o "$dir/cfrweb.mo" "$po_file"
done
