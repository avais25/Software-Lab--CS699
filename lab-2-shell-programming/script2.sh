#!/bin/bash
echo "This script will create a backup of all the .doc file fom Downloads folder to doc.zip which will be stored in home directory"
ls ~/Downloads/*.doc | xargs -I % zip -u doc.zip '%'

