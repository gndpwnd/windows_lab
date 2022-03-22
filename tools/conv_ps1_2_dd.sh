#!/bin/bash
in_file=$1
dest_file=$2

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage()
{
echo -e "
${NC}usage: $0 <ps1 script> <dd file>

OPTIONS:
	-h				Display this menu
   	
	-i FILE		 	PowerShell script to convert
   	
	-o FILE  		resulting .dd file
   
EXAMPLE USAGE:

	conv_ps1_2_dd.sh lol.ps1 lol.dd
"
}

inf=
otf=


while getopts “:hi:o:” OPTION
do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    i)
      inf=$OPTARG
      ;;
    o)
      otf=$OPTARG
      ;;
  esac
done

if [ -z $inf ]; then
	printf "${RED}[x] No input file provided..."
	usage
	exit 1
elif [ -z $otf ]; then
	printf "${RED}[x] No output file provided..."
	usage
	exit 1
fi

echo -e "
DELAY 750
GUI r
DELAY 1000
STRING powershell Start-Process notepad -Verb runAs
ENTER" > $otf

while read -r line;
do
   echo "String ${line}"
   echo "ENTER"
done < $inf >> $otf
