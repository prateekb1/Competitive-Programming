from datetime import datetime as dt

def timedelta(t1,t2):
    # Sat 10 May 2015 19:54:36 +0530
    # %a  %d %B  %Y   %H:%M:%S %z
    first = dt.strptime(t1,"%a  %d %B    %Y   %H:%M:%S %z")
    second =dt.strptime(t2,"%a  %d %B  %Y   %H:%M:%S %z")
    return str(abs(int((first-second).total_seconds())))
    
print(timedelta("Sun 2 March 2015 13:54:36 -0700","Sat 10 May 2015 19:54:36 +0530"))