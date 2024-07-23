#!/users/allehe/python3/bin/python3.8

from datetime import datetime,timezone
import time
import pytz

def chooseIntLoop( options:list, prompt:str="Please input a valid choice", head:str="", rvt:str='int' ) ->int:
    """
        This is a main choose function for user to select from a list of actions which indexed with int number like:
        [1] sth
        [2] sth
        [3] sth
        [4] sth
        Parameter:
        options:list --- a list of choices for user to select. the order in list will be the actual order
            [thing1,thing2,thin3,thing4]
    """
    size = len(options)
    while True:
        #----Generate the options menu
        print("--------------------------")
        print()
        if head != "":print(f'\t\t***{head}***')
        #range started from 0, so range(size) match the order in list
        for i in range(size):
            print(f"\t[{i+1}] {options[i]}")
        #print("--------------------------")
        print()
        choose = input( "----------------: " + prompt + f" <from 1 to {size}>: " )
        if choose.isdigit():
            if int(choose) in [ x+1 for x in range(size) ]:
                if rvt == 'int':
                    return int(choose)
                elif rvt == 'value':
                    return options[ int(choose) - 1 ]
            else:
                print(f"\t\t[{choose}] out of range, please input again...")
        else:
            print(f"\t\t[{choose}] is not a valid number, please input again...")
        print()

def showTime( mytime, end=None )->None:
    """
        Purpose:
            Return date and time in several predefined timezone based on a given time.
        parameter:
            mytime: this should be a datatime object which include tzone information
        return:
            None
    """

    # Pre-defined timezone to show as a result
    utc = pytz.utc
    bj = pytz.timezone('Asia/Shanghai')
    jp = pytz.timezone('Asia/Tokyo')
    india = pytz.timezone('Asia/Kolkata')
    bru = pytz.timezone('Europe/Brussels')
    mtv = pytz.timezone('America/Los_Angeles')
    #rtp = pytz.timezone('America/New_York')
    # If I use above timezone name, the %Z in strftime will show LMT rather than EDT
    rtp = pytz.timezone('America/Indiana/Indianapolis')
    syd = pytz.timezone('Australia/Sydney')

    # Show the result

    to = lambda t,z : t.astimezone(z).strftime("[%Y-%m-%d] [%H:%M] %Z %z")
    if end == None:
        print()
        print(f'Source Time Zone:   {mytime.tzname()}')
        print(f'Source Time:        {mytime.ctime()}')
        now = mytime
        print()
        print('---- Adjusted Times In Different Time Zone ----')
        print(f'MTV Time:     {to(now,mtv)}')
        print(f'RTP Time:     {to(now,rtp)}')
        #print(f'RTP Time:     {now.astimezone(rtp)}')
        print(f'UTC Time:     {to(now,utc)}')
        print(f'Brussels Time:{to(now,bru)}')
        print(f'India Time:   {to(now,india)}')
        print(f'Beijing Time: {to(now,bj)}')
        print(f'Japan Time:   {to(now,jp)}')
        print(f'SYD Time:     {to(now,syd)}')
    else:
        #to2 = lambda st,et,z : 'From: ' + str(st.astimezone(z).strftime("[%Y-%m-%d] [%H:%M] %Z")) + ' To: [' + str(et.astimezone(z).strftime) + ']'
        to2 = lambda st,et,z : f'From: {str( to(st,z) ):<32} To: {str( to(et,z) )}'
        print()
        print(f'Starting Time: {mytime.ctime()} TimeZone: {mytime.tzname()}')
        print(f'Ending   Time: {end.ctime()} TimeZone: {end.tzname()}')
        print()
        print('---- Adjusted Times In Different Time Zone ----')
        print(f'MTV Time:     {to2(mytime,end,mtv)}')
        print(f'RTP Time:     {to2(mytime,end,rtp)}')
        print(f'UTC Time:     {to2(mytime,end,utc)}')
        print(f'Brussels Time:{to2(mytime,end,bru)}')
        print(f'India Time:   {to2(mytime,end,india)}')
        print(f'Beijing Time: {to2(mytime,end,bj)}')
        print(f'Japan Time:   {to2(mytime,end,jp)}')
        print(f'SYD Time:     {to2(mytime,end,syd)}')


def getTime( prompt:str, tzs:list ) -> datetime:
    while True:
        try:
            utime = input(prompt)
            ptime = datetime.strptime( utime, '%Y-%m-%d %H:%M' )
            break
        except Exception as e:
            print(e)
    tzs = tzs
    utz = chooseIntLoop( tzs, rvt='value')
    utz = pytz.timezone(utz)
    ptime = utz.localize(ptime)
    return ptime

if __name__ == '__main__':
    menu = ['Use local system time',
            'Specify a time in a specific time zone',
            'Specify a time range in a specific time zone']
    head = "Time Zone Convert Tool"
    #choice = chooseIntLoop( menu )
    choice = chooseIntLoop( menu, head=head )
    tzs = ['America/Los_Angeles','America/New_York','Europe/Brussels','Asia/Kolkata','Asia/Shanghai','Asia/Tokyo','Australia/Sydney']

    if choice == 1:
        ut = datetime.now(timezone.utc)
        lt = ut.astimezone()
        showTime( lt )
    elif choice == 2:
      ptime = getTime("Please Input Time (valid format: 2021-2-1 18:30): ",tzs)
      showTime( ptime )
    elif choice == 3:
        stime = getTime("Please Input Starting Time (valid format: 2021-2-1 18:30): ",tzs)
        etime = getTime("Please Input Ending Time (valid format: 2021-2-1 18:30): ",tzs)
        showTime( stime, etime )

