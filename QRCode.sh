#!/bin/bash
echo "Reading QRCode."
zbarcam --nodisplay --raw > QRCodes.txt &
PID=$!
sleep 5
kill $PID
if [ -s QRCodes.txt ] ; then
  echo "QRCode was successfully read."
else
  echo "Problems reading the QRCode."
fi
#rm -rf QRCodes.txt
