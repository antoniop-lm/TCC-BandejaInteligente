file = open("Localizations.txt", "r")
text = file.readlines()
file.close()

FstLocal = text[0][13:]
SndLocal = text[1][13:]
TrdLocal = text[2][13:]
FinalLocal = ""

if (FstLocal == SndLocal):
  if (FstLocal == TrdLocal):
    FinalLocal = "It's in " + FstLocal
  else:
    FinalLocal = "Somewhere near " + FstLocal + " and " + TrdLocal + "."
else:
  if (FstLocal == TrdLocal):
    FinalLocal = "Somewhere near " + FstLocal + " and " + SndLocal + "."
  else:
    FinalLocal = "We can't determinate exactly where it was suppose to be."

file = open("Localization.txt", "w")
file.write(FinalLocal)
file.close()