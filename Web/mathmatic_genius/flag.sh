#!/bin/sh

if [ -z "${GZCTF_FLAG}" ]; then
	$GZCTF_FLAG = "catctf{this_is_test_flag_for_ez_code}"
fi

echo $GZCTF_FLAG > /flag

chmod 755 /flag

unset GZCTF_FLAG

rm -f /flag.sh
