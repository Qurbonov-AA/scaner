import csv
list_cvf = []
path = "C:/Users/User/Desktop/bot/Qt/scaner/result.log"


def read_file(path):
    with open(path,mode = "r+", encoding = 'ascii') as f:
        for log_list in f:
            log = log_list.replace("<0x1D>",chr(29)) 
            index = log.find("|")
            log = log[:index]
            list_cvf.append(log)
    
    return list_cvf

def write_csv(logs):
    csvfile = open('convert.csv', mode = 'wb')
    writer = csv.writer(csvfile)
    for item in set(logs):
        item = item.split()       
        writer.writerow(item)


logs = read_file(path)
write_csv(logs)
