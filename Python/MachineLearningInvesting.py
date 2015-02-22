# use ML with debt/equity ratio as a feature to determine buy/sell rating for stock

import pandas as pd
import os
import time
from datetime import datetime

path = "/Users/Max/SkyDrive/Programming/GitHub/intraQuarter"

def Key_Stats(gather = "Total Debt/Equity (mrq)"):
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]  # all company directories

    for each_dir in stock_list[1:]:  # first elt is root directory itself
        each_file = os.listdir(each_dir)
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unixTime = time.mktime(date_stamp.timetuple())
                print(date_stamp, unixTime)
                time.sleep(15)



Key_Stats()

