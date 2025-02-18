"""
The simplest example of reading a tag from a PLC

NOTE: You only need to call .Close() after you are done exchanging
data with the PLC.  If you were going to read in a loop or read
more tags, you wouldn't want to call .Close() every time.
"""
from pylogix import PLC

if __name__=='__main__':
    comm = PLC()
    comm.IPAddress = '127.0.0.1'
    ret = comm.Read('CurrentScreen')
    print(ret.Value)
    comm.Close()
