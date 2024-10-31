#!/bin/sh

if [ -z "${GZCTF_FLAG}" ]; then
    echo "<?php \$flag = \"catctf{PHp_We0kCompa4e_s0_1nteresting} \"; ?>" > /var/www/html/flag.php
    exit 1
fi
echo "<?php \$flag = \"${GZCTF_FLAG}\"; ?>" > /var/www/html/flag.php
