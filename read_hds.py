import csv
from glob import glob
from datetime import datetime

column_map = {
    "DP Pool":"DP_Pool",
    "IO Rate(IOPS)":"IO_Rate(IOPS)",
    "Read Rate(IOPS)":"Read_Rate(IOPS)",
    "Write Rate(IOPS)":"Write_Rate(IOPS)",
    "Read Hit(%)":"Read_Hit(%)",
    "Write Hit(%)":"Write_Hit(%)",
    "Trans. Rate(MB/S)":"Trans._Rate(MB/S)",
    "Read Trans. Rate(MB/S)":"Read_Trans._Rate(MB/S)",
    "Write Trans. Rate(MB/S)":"Write_Trans._Rate(MB/S)",
    "Read CMD Count":"Read_CMD_Count",
    "Write CMD Count":"Write_CMD_Count",
    "Read CMD Hit Count":"Read_CMD_Hit_Count",
    "Write CMD Hit Count":"Write_CMD_Hit_Count",
    "Read Trans. Size(MB)":"Read_Trans._Size(MB)",
    "Write Trans. Size(MB)":"Write_Trans._Size(MB)",
    "CTL CMD IO Rate(IOPS)":"CTL_CMD_IO_Rate(IOPS)",
    "CTL CMD Trans. Rate(KB/S)":"CTL_CMD_Trans._Rate(KB/S)",
    "CTL CMD Count":"CTL_CMD_Count",
    "CTL CMD Trans. Size(KB)":"CTL_CMD_Trans._Size(KB)",
    "CTL CMD Time(microsec.)":"CTL_CMD_Time(microsec.)",
    "CTL CMD Max Time(microsec.)":"CTL_CMD_Max_Time(microsec.)",
    "Data CMD IO Rate(IOPS)":"Data_CMD_IO_Rate(IOPS)",
    "Data CMD Trans. Rate(MB/S)":"Data_CMD_Trans._Rate(MB/S)",
    "Data CMD Count":"Data_CMD_Count",
    "Data CMD Trans. Size(MB)":"Data_CMD_Trans._Size(MB)",
    "Data CMD Time(microsec.)":"Data_CMD_Time(microsec.)",
    "Data CMD Max Time(microsec.)":"Data_CMD_Max_Time(microsec.)",
    "Timeout Error Count":"Timeout_Error_Count",
    "Random IO Rate(IOPS)":"Random_IO_Rate(IOPS)",
    "Random Read Rate(IOPS)":"Random_Read_Rate(IOPS)",
    "Random Write Rate(IOPS)":"Random_Write_Rate(IOPS)",
    "Random Trans. Rate(MB/S)":"Random_Trans._Rate(MB/S)",
    "Random Read Trans. Rate(MB/S)":"Random_Read_Trans._Rate(MB/S)",
    "Random Write Trans. Rate(MB/S)":"Random_Write_Trans._Rate(MB/S)",
    "Random Read CMD Count":"Random_Read_CMD_Count",
    "Random Write CMD Count":"Random_Write_CMD_Count",
    "Random Read Trans. Size(MB)":"Random_Read_Trans._Size(MB)",
    "Random Write Trans. Size(MB)":"Random_Write_Trans._Size(MB)",
    "Sequential IO Rate(IOPS)":"Sequential_IO_Rate(IOPS)",
    "Sequential Read Rate(IOPS)":"Sequential_Read_Rate(IOPS)",
    "Sequential Write Rate(IOPS)":"Sequential_Write_Rate(IOPS)",
    "Sequential Trans. Rate(MB/S)":"Sequential_Trans._Rate(MB/S)",
    "Sequential Read Trans. Rate(MB/S)":"Sequential_Read_Trans._Rate(MB/S)",
    "Sequential Write Trans. Rate(MB/S)":"Sequential_Write_Trans._Rate(MB/S)",
    "Sequential Read CMD Count":"Sequential_Read_CMD_Count",
    "Sequential Write CMD Count":"Sequential_Write_CMD_Count",
    "Sequential Read Trans. Size(MB)":"Sequential_Read_Trans._Size(MB)",
    "Sequential Write Trans. Size(MB)":"Sequential_Write_Trans._Size(MB)",
    "XCOPY Rate(IOPS)":"XCOPY_Rate(IOPS)",
    "XCOPY Read Rate(IOPS)":"XCOPY_Read_Rate(IOPS)",
    "XCOPY Write Rate(IOPS)":"XCOPY_Write_Rate(IOPS)",
    "XCOPY Read Trans. Rate(MB/S)":"XCOPY_Read_Trans._Rate(MB/S)",
    "XCOPY Write Trans. Rate(MB/S)":"XCOPY_Write_Trans._Rate(MB/S)",
    "XCOPY Time(microsec.)":"XCOPY_Time(microsec.)",
    "XCOPY Max Time(microsec.)":"XCOPY_Max_Time(microsec.)",
    "Read CMD Hit Count2":"Read_CMD_Hit_Count2",
    "Read CMD Hit Time(microsec.)":"Read_CMD_Hit_Time(microsec.)",
    "Read CMD Hit Max Time(microsec.)":"Read_CMD_Hit_Max_Time(microsec.)",
    "Write CMD Hit Count2":"Write_CMD_Hit_Count2",
    "Write CMD Hit Time(microsec.)":"Write_CMD_Hit_Time(microsec.)",
    "Write CMD Hit Max Time(microsec.)":"Write_CMD_Hit_Max_Time(microsec.)",
    "Read CMD Miss Count":"Read_CMD_Miss_Count",
    "Read CMD Miss Time(microsec.)":"Read_CMD_Miss_Time(microsec.)",
    "Read CMD Miss Max Time(microsec.)":"Read_CMD_Miss_Max_Time(microsec.)",
    "Write CMD Miss Count":"Write_CMD_Miss_Count",
    "Write CMD Miss Time(microsec.)":"Write_CMD_Miss_Time(microsec.)",
    "Write CMD Miss Max Time(microsec.)":"Write_CMD_Miss_Max_Time(microsec.)",
    "Read CMD Job Count":"Read_CMD_Job_Count",
    "Read CMD Job Time(microsec.)":"Read_CMD_Job_Time(microsec.)",
    "Read CMD Job Max Time(microsec.)":"Read_CMD_Job_Max_Time(microsec.)",
    "Write CMD Job Count":"Write_CMD_Job_Count",
    "Write CMD Job Time(microsec.)":"Write_CMD_Job_Time(microsec.)",
    "Write CMD Job Max Time(microsec.)":"Write_CMD_Job_Max_Time(microsec.)",
    "Read Hit Delay CMD Count(<300ms)":"Read_Hit_Delay_CMD_Count(<300ms)",
    "Read Hit Delay CMD Count(300-499ms)":"Read_Hit_Delay_CMD_Count(300-499ms)",
    "Read Hit Delay CMD Count(500-999ms)":"Read_Hit_Delay_CMD_Count(500-999ms)",
    "Read Hit Delay CMD Count(1000ms-)":"Read_Hit_Delay_CMD_Count(1000ms-)",
    "Write Hit Delay CMD Count(<300ms)":"Write_Hit_Delay_CMD_Count(<300ms)",
    "Write Hit Delay CMD Count(300-499ms)":"Write_Hit_Delay_CMD_Count(300-499ms)",
    "Write Hit Delay CMD Count(500-999ms)":"Write_Hit_Delay_CMD_Count(500-999ms)",
    "Write Hit Delay CMD Count(1000ms-)":"Write_Hit_Delay_CMD_Count(1000ms-)",
    "Read Miss Delay CMD Count(<300ms)":"Read_Miss_Delay_CMD_Count(<300ms)",
    "Read Miss Delay CMD Count(300-499ms)":"Read_Miss_Delay_CMD_Count(300-499ms)",
    "Read Miss Delay CMD Count(500-999ms)":"Read_Miss_Delay_CMD_Count(500-999ms)",
    "Read Miss Delay CMD Count(1000ms-)":"Read_Miss_Delay_CMD_Count(1000ms-)",
    "Write Miss Delay CMD Count(<300ms)":"Write_Miss_Delay_CMD_Count(<300ms)",
    "Write Miss Delay CMD Count(300-499ms)":"Write_Miss_Delay_CMD_Count(300-499ms)",
    "Write Miss Delay CMD Count(500-999ms)":"Write_Miss_Delay_CMD_Count(500-999ms)",
    "Write Miss Delay CMD Count(1000ms-)":"Write_Miss_Delay_CMD_Count(1000ms-)",
    "Read Job Delay CMD Count(<300ms)":"Read_Job_Delay_CMD_Count(<300ms)",
    "Read Job Delay CMD Count(300-499ms)":"Read_Job_Delay_CMD_Count(300-499ms)",
    "Read Job Delay CMD Count(500-999ms)":"Read_Job_Delay_CMD_Count(500-999ms)",
    "Read Job Delay CMD Count(1000ms-)":"Read_Job_Delay_CMD_Count(1000ms-)",
    "Write Job Delay CMD Count(<300ms)":"Write_Job_Delay_CMD_Count(<300ms)",
    "Write Job Delay CMD Count(300-499ms)":"Write_Job_Delay_CMD_Count(300-499ms)",
    "Write Job Delay CMD Count(500-999ms)":"Write_Job_Delay_CMD_Count(500-999ms)",
    "Write Job Delay CMD Count(1000ms-)":"Write_Job_Delay_CMD_Count(1000ms-)",
    "Tag Count":"Tag_Count",
    "Average Tag Count":"Average_Tag_Count",
    "Total Tag Count":"Total_Tag_Count",
    "Read Tag Count":"Read_Tag_Count",
    "Write Tag Count":"Write_Tag_Count",
    "Total Average Tag Count":"Total_Average_Tag_Count",
    "Read Average Tag Count":"Read_Average_Tag_Count",
    "Write Average Tag Count":"Write_Average_Tag_Count",
    "Write Pending Rate(%)":"Write_Pending_Rate(%)",
    "Clean Queue Usage Rate(%)":"Clean_Queue_Usage_Rate(%)",
    "Middle Queue Usage Rate(%)":"Middle_Queue_Usage_Rate(%)",
    "Physical Queue Usage Rate(%)":"Physical_Queue_Usage_Rate(%)",
    "Total Queue Usage Rate(%)":"Total_Queue_Usage_Rate(%)",
    "Partition Write Pending Rate(%)":"Partition_Write_Pending_Rate(%)",
    "Partition Clean Queue Usage Rate(%)":"Partition_Clean_Queue_Usage_Rate(%)",
    "Core Usage(%)":"Core_Usage(%)",
    "Host-Cache Bus Usage Rate(%)":"Host-Cache_Bus_Usage_Rate(%)",
    "Drive-Cache Bus Usage Rate(%)":"Drive-Cache_Bus_Usage_Rate(%)",
    "Processor-Cache Bus Usage Rate(%)":"Processor-Cache_Bus_Usage_Rate(%)",
    "Bus Usage Rate(%)":"Bus_Usage_Rate(%)",
    "Dual Bus Usage Rate(%)":"Dual_Bus_Usage_Rate(%)",
    "Total Bus Usage Rate(%)":"Total_Bus_Usage_Rate(%)",
    "IO Rate(IOPS)":"IO_Rate(IOPS)",
    "Online Verify Rate(IOPS)":"Online_Verify_Rate(IOPS)",
    "Read Trans. Size":"Read_Trans._Size",
    "Write Trans. Size":"Write_Trans._Size",
    "Online Verify CMD Count":"Online_Verify_CMD_Count",
    "Operating Rate(%)":"Operating_Rate(%)",
    "Unload Time(min.)":"Unload_Time(min.)"}

current_section = None
headers_done = False
data_output = dict()
start_date = None
end_data = None

# Get the performance files we're going to read
perf_files = glob('pfm*')

def fix_column_names(data_line):
    """ We need to actually replace the spaces with _ for the column
        names since Hitachi doesn't use a fixed width OR tab delimination
        If we don't we can't parse cleanly with the csv module """

    sorted_keys = column_map.keys()
    sorted_keys.sort(lambda x,y: cmp(len(y), len(x)))
    for colname in sorted_keys:
        if colname in data_line:
            data_line = data_line.replace(colname,column_map[colname])

    return data_line

def calc_interval(d1, d2):
    global start_date
    global end_date
    """ Calculates the interval between two ~ ISO dates that HDS uses
        YYYY/MM/DD HH:MM:SS """

    dt1 = datetime.strptime(d1,"%Y/%m/%d %H:%M:%S")
    dt2 = datetime.strptime(d2,"%Y/%m/%d %H:%M:%S")

    if not start_date:
        start_date = dt1
        end_date = dt2
    else:
        if dt1 < start_date:
           start_date = dt1
        if dt2 > end_date:
           end_date = dt2

    return abs((dt2-dt1).seconds)

def parse_file_line(data_line):
    data_line = data_line.translate(None, '\x00').rstrip()
    global current_section
    if '----' in data_line:    # Data Section Descriptor
        current_section = data_line.replace('---- ','').replace(' ----','').rstrip()
        data_output[current_section] = dict()
        data_output[current_section]['data'] = dict()
        data_output[current_section]['headers'] = []
    elif 'CTL' in data_line:    # Column headers
        data_line = fix_column_names(data_line)
        if "Port" in current_section or "RG" in current_section or "DP" in current_section or "LU" in current_section or "Backend" in current_section:
            line = data_line.split()
            if data_output[current_section]["headers"] == []:
                data_output[current_section]["headers"].extend(line)
            else:
                data_output[current_section]["headers"].extend(line[2:])
        if "Drive Info" in current_section:
            line = data_line.split()
            if data_output[current_section]["headers"] == []:
                data_output[current_section]["headers"].extend(line)
            else:
                data_output[current_section]["headers"].extend(line[3:])
    else:
        if "Port" in current_section or "RG" in current_section or "DP" in current_section or "LU" in current_section or "Backend" in current_section:
            line = data_line.split()
            ctl = line.pop(0)
            port = line.pop(0)

            # Setup the datastructure
            if ctl not in data_output[current_section]["data"]:
                data_output[current_section]["data"][ctl] = dict() 
            if port not in data_output[current_section]["data"][ctl]:
                data_output[current_section]["data"][ctl][port] = list()

            data_output[current_section]["data"][ctl][port].extend(line)
        if "Drive Info" in current_section:
            line = data_line.split()
            ctl = line.pop(0)
            unit = line.pop(0)
            hdu = line.pop(0)

            # Setup the datastructure
            if ctl not in data_output[current_section]["data"]:
                data_output[current_section]["data"][ctl] = dict() 
            if unit not in data_output[current_section]["data"][ctl]:
                data_output[current_section]["data"][ctl][unit] = dict()
            if hdu not in data_output[current_section]["data"][ctl][unit]:
                data_output[current_section]["data"][ctl][unit][hdu] = list()

            data_output[current_section]["data"][ctl][unit][hdu].extend(line)
 
# Open each file and process the data in it

complete_output = dict()

for perf in perf_files:
    with open(perf, 'rb') as f:
    
       file_data = f.readlines()

       # Some basic info we'll need
       file_name = perf
       file_number = file_data.pop(0).replace("No.","")
       file_info = file_data.pop(0).split(' - ')
       file_interval = calc_interval(file_info[0],file_info[1])
       file_serial = file_info[2].rstrip().replace("SN:","")

       print "Parsing File: %s  Sequence #: %s  Start Time: %s   End Time: %s" % (perf,file_number, file_info[0], file_info[1])
       for line in file_data:
           parse_file_line(line)

       for i in data_output.keys():
             if i not in complete_output:
                 complete_output[i] = dict()
             if "headers" not in complete_output[i]:
                 complete_output[i]["headers"] = data_output[i]["headers"]
             if "data" not in complete_output[i]:
                 complete_output[i]["data"] = dict()
             if "Port" in i or "RG" in i or "DP" in i or "LU" in i or "Backend" in i:
                 port_data = list()
                 for ctl in data_output[i]["data"].keys():
                     for port in data_output[i]["data"][ctl].keys(): 
                         output = [ctl, port]
                         output.extend(data_output[i]["data"][ctl][port])
                         port_data.append(output)

                 if file_info[1] not in complete_output[i]["data"]:
                     complete_output[i]["data"][file_info[1]] = list()                 

                 complete_output[i]["data"][file_info[1]].extend(port_data)

             if "Drive Info" in i:
                 drive_data = list()
                 for ctl in data_output[i]["data"].keys():
                     for unit in data_output[i]["data"][ctl].keys(): 
                         for hdu in data_output[i]["data"][ctl][unit].keys():
                             output = [ctl, unit, hdu]
                             output.extend(data_output[i]["data"][ctl][unit][hdu])
                             drive_data.append(output)

                 if file_info[1] not in complete_output[i]["data"]:
                     complete_output[i]["data"][file_info[1]] = list()                 

                 complete_output[i]["data"][file_info[1]].extend(drive_data)

for i in complete_output.keys():
    output_file = "HDS_%s_%s.csv" % (file_serial, i.replace(' ','_'))
    print i
    print "Outputting to: %s" % output_file
    with open(output_file,'wb') as f:
        f.write("Array Serial,%s,Collection Start,%s,Collection End,%s\n" % (file_serial,start_date,end_date))
        f.write("Timestamp,")
        f.write(",".join(complete_output[i]["headers"]))
        f.write("\n")
        for j in complete_output[i]["data"].keys():
            for k in complete_output[i]["data"][j]:
                f.write("%s," % j)
                f.write(",".join(k))
                f.write("\n")
         
