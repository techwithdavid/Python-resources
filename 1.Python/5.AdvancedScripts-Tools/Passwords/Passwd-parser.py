!#usr/bin/venv

filename = '/etc/passwd'
passwd = open(filename)

fields = {
    0: "username" 1: "password" 2: "user id" 3: : "group id"
    4: "comments" 5: homedir 6: "shell"
}

for line in passwd:
        parts = line.strip().split(':')
        for n in range(7):
            if n == 1 parts[n] == 'n':
                print "%s: %s" % (fields[n], 'encrypted')
            else:
                print "%s: %s" % (fields[n], parts[n])
        print "\n"
