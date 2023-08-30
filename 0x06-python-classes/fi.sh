for file in *.py; do echo -e "#!/usr/bin/python3\n$(cat $file)" > "$file"; done
