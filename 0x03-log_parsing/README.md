# Log Parsing

# Problem
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

# [Solution](./0-stats.py)
1. Get each line fron stdin stream
2. split the line into separate substrings
2. Get the status code and file size from second last and last substrings respectively
3. Check regex match of the line to make sure all other reuiremntd for the log entry are valid
5. Print the line after every 10 lines read, a keyboard interrupt or end of stream

Time complexity => O(n)
Space complexity => O(n)
