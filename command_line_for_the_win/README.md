command_line_for_the_win

File Transfer Using SFTP

1. Open a terminal or command prompt on the local machine.
2.  Copy and use the SFTP command-line tool to establish a connection to the sandbox environment with `sftp username@hostname`.
3. You will be promoted to type in the password
4. Navigate to the directory where you want to upload the screenshots with `cd’
5.  Use the SFTP `put` command to upload the screenshots from the local machine to the sandbox environment(you have to specify the path) with `put /Users/YourUsername/folder/screenshot.png`.
6. Confirm the successful transfer of the screenshots by checking the sandbox directory with `ls`
