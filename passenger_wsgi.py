import sys, os
INTERP = os.path.join(os.environ['HOME'], '<REPLACE WITH URL>', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


sys.path.append('app')
from app.app import app as application