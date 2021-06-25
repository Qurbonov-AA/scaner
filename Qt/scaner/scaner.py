import csv
list_cvf = []
path = "result.log"
def read_file(path):
    with open(path,"r+") as f:
        for log_list in f:
            log = log_list.replace("<0x1D>","") 
            index = log.find("|")
            log = log[:index]
            list_cvf.append(log)
    return list_cvf

def write_csv(logs):
    csvfile = open('convert.csv', 'w', newline= '')
    writer = csv.writer(csvfile)
    for item in logs:
        item = item.split()       
        writer.writerow(item)

read_file(path)
write_csv(list_cvf)
