#!/bin/bash
echo "Tracking the tray."
sudo ./findclient -g USP --nodebug > Localizations.txt
if [ -s Localizations.txt ] ; then
  python ParseLocalizations.py
  echo "The tray was successfully tracked."
else
  echo "Problems tracking the tray."
fi
rm -rf Localizations.txt
