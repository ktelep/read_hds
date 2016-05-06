read_hds.py
------------

Simple parser for HDS Performance Data files (listed out as prf######.txt) to convert them to CSV

Drop the script into the directory with the data and run it.   A CSV file will be created for each type of object (Disks, LUs, Ports, etc.) that can then be opened in Excel, Pandas, Access, any Database, etc. for further number crunching.

NOte:  Currently Cache and Processor performance numbers are not parsed


Written by Kurt Telep

Sample Output
--------------

    PS C:\Users\ktele\workspace\HDSAnalysis> dir


    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    -a----         5/6/2016  11:06 AM        2129541 pfm00000.txt
    -a----         5/6/2016  11:06 AM        2129541 pfm00001.txt
    -a----         5/6/2016  11:06 AM        2129541 pfm00002.txt
    -a----         5/6/2016  11:06 AM        2129541 pfm00003.txt
    -a----         5/6/2016  11:06 AM        2129541 pfm00004.txt
    -a----         5/6/2016  11:06 AM        2129541 pfm00005.txt
    -a----         5/6/2016   5:10 PM            395 README.md
    -a----         5/6/2016   5:06 PM          14846 read_hds.py
    
    
    PS C:\Users\ktele\workspace\HDSAnalysis> .\read_hds.py
    Parsing File: pfm00000.txt  Sequence #: 1
      Start Time: 2016/05/03 07:35:19   End Time: 2016/05/03 07:40:20
    Parsing File: pfm00001.txt  Sequence #: 2
      Start Time: 2016/05/03 07:40:20   End Time: 2016/05/03 07:45:28
    Parsing File: pfm00002.txt  Sequence #: 3
      Start Time: 2016/05/03 07:45:28   End Time: 2016/05/03 07:50:19
    Parsing File: pfm00003.txt  Sequence #: 4
      Start Time: 2016/05/03 07:50:19   End Time: 2016/05/03 07:55:19
    Parsing File: pfm00004.txt  Sequence #: 5
      Start Time: 2016/05/03 07:55:19   End Time: 2016/05/03 08:00:19
    Parsing File: pfm00005.txt  Sequence #: 6
      Start Time: 2016/05/03 08:00:19   End Time: 2016/05/03 08:05:22
    Cache Information
    Outputting to: HDS_00000000_Cache_Information.csv
    Backend Information
    Outputting to: HDS_00000000_Backend_Information.csv
    DP Pool Information
    Outputting to: HDS_00000000_DP_Pool_Information.csv
    RG Information
    Outputting to: HDS_00000000_RG_Information.csv
    Processor Information
    Outputting to: HDS_00000000_Processor_Information.csv
    Port Information
    Outputting to: HDS_00000000_Port_Information.csv
    Drive Information
    Outputting to: HDS_00000000_Drive_Information.csv
    LU Information
    Outputting to: HDS_00000000_LU_Information.csv
    Drive Operate Information
    Outputting to: HDS_00000000_Drive_Operate_Information.csv
    PS C:\Users\ktele\workspace\HDSAnalysis>
