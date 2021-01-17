hsel *fits $I "OBJECT=='bias'" > zero.list
hsel *fits $I "OBJECT=='flat'" > flat.list
hsel *fits $I "IMAGETYPE=='OBJECT'" > objall.list
hsel *fits $I "IMAGETYPE=='COMP'" > lampall.list
cat flat.list lampall.list objall.list > flatnall.list
cat objall.list lampall.list > specall.list
