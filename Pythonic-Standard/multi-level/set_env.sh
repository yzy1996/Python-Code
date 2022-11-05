# put project directory into PYTHONPATH

DIR="$(pwd)"
export PYTHONPATH="${DIR}":$PYTHONPATH
echo "added $DIR to PYTHONPATH"