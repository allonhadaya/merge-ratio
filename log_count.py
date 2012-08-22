import os
import subprocess as sp

def count(type):
    logs = sp.Popen(['git','log',type,'--oneline'], stdout=sp.PIPE)
    count = sp.Popen(['wc','-l'], stdin=logs.stdout, stdout=sp.PIPE)
    return count.communicate()[0]
    
def merges():
    return float(count('--merges'))

def no_merges():
    return float(count('--no-merges'))

def count_each():
    for dir in filter(os.path.isdir, os.listdir('.')):
        os.chdir(dir)
        if '.git' in os.listdir('.'):
	    m = merges()
            yield (m/(m + no_merges()), dir)
	os.chdir('..')

for r in sorted(count_each(), reverse=True):
    print "{0:.1%}\t{1}".format(r[0], r[1])
