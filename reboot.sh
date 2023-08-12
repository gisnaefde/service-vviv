#!/bin/bash

# Batas penggunaan memori (dalam persen)
LIMIT=80

while true; do
    # Hitung penggunaan memori saat ini
    usage=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

    # Cetak penggunaan memori
    echo "Memory usage: $usage%"

    # Cek jika penggunaan memori melebihi batas
    if awk -v usage="$usage" -v limit="$LIMIT" 'BEGIN {exit usage>limit ? 0 : 1}'; then
        # Jika ya, lakukan restart
        echo "Memory limit exceeded, restarting"
        sudo /sbin/shutdown -r now
    fi

    # Tunggu 1 detik
    sleep 60
done
