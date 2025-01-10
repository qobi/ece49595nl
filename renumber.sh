#!/bin/bash
for f in {h,l}*.tex; do
    sed -e "s/2024/2025/g" ../spring2024/$f >$f
done
