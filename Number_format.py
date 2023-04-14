def format_point(number):
    return "{:,}".format(round(number)).replace(',','~').replace('.',',').replace('~','.')

