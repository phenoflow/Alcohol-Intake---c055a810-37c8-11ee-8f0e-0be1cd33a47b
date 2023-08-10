# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"1361.11","system":"readv2"},{"code":"1361.12","system":"readv2"},{"code":"136A.00","system":"readv2"},{"code":"136B.00","system":"readv2"},{"code":"136C.00","system":"readv2"},{"code":"136G.00","system":"readv2"},{"code":"136J.00","system":"readv2"},{"code":"136N.00","system":"readv2"},{"code":"136O.00","system":"readv2"},{"code":"136R.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-intake-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol-intake-drinker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol-intake-drinker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol-intake-drinker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
