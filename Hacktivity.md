1)) If you get a reverse shell you know what that's look like without meterpreter or something. If you want to get a stable,interactive bash shell and if python is 
supported, then
> python -c "import pty; pty.spawn('/bin/bash')"

2)) Sometimes i get confused with smbclient. So this note is for mine.
> smbclient -L $IP$or$domain$
> smbclient \\\\$IP$or$domain$\share

For downloading a file from remote server,
> get file
For uploading a file to remote server,
> put file
