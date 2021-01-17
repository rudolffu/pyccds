hsel *fits $I "OBJECT=='bias'" > zero.list
hsel *fits $I "OBJECT=='istflat'" > flat.list
hsel *fits $I "(IMAGETYPE=='OBJECT')&(OBJECT!='istflat')" > objall.list
hsel *fits $I "IMAGETYPE=='COMP'" > lampall.list
cat flat.list lampall.list objall.list > flatnall.list
cat objall.list lampall.list > specall.list
