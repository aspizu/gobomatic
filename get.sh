function getstatementblocks {
    for i in $(grep -oP '(?<=def\s)[a-zA-Z_]*(?=\(.*\)\s\-\>\sStatementBlock\:)' "$1"); do
        echo "    '$(echo "${i,,}")': gm.$i,"
    done
}

function getreporterblocks {
    for i in $(grep -oP '(?<=def\s)[a-zA-Z_]*(?=\(.*\)\s\-\>\sReporterBlock\:)' "$1"); do
        echo "    '$(echo "${i,,}")': gm.$i,"
    done
}

files="motion.py control.py looks.py operator.py pen.py sensing.py events.py motion.py\
            otherblocks.py sa.py sound.py"

echo "import gobomatic as gm"
echo
echo "STATEMENT_BLOCKS = {"
for file in $files; do
    getstatementblocks gobomatic/blocks/$file
done
echo "}"
echo
echo
echo "REPORTER_BLOCKS = {"
for file in $files; do
    getreporterblocks gobomatic/blocks/$file
done
echo "}"
