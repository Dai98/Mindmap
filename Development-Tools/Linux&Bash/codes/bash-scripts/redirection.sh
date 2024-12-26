#!/usr/bin/bash

rm -f hello.txt

# > symbol
echo Hello World! > hello.txt

# >> symbol
echo Hello Output Redirection >> hello.txt

# | operator
cat hello.txt | grep Hello

# < operator
wc -w < hello.txt

# << operator
cat << EOF
Try to enter
multiple line
until I enter
EOF

# <<< operator
wc -w <<< "Hello input redirection"
