from pylogix import PLC

if __name__ == '__main__':
    comm = PLC()
    comm.IPAddress = '127.0.0.1'
    ret = comm.Read('DINT1')
    print(ret.TagName, ret.Value, ret.Status)
    comm.Close()
