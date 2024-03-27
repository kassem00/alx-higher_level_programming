for file in *.js ;do
  echo '#!/usr/bin/node' > "$file"
done
chmod u+x *.js
