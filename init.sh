python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt
DIR="certs"
FILE="thingName.txt"
thingFile="$DIR/$FILE"
if [ -d "$DIR" ]; then
  if [ ! -f "$thingFile" ]; then
      pushd "$DIR"
        touch $FILE
      popd
  fi
fi
