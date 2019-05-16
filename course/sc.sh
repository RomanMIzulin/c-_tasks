#!/bin/bash
cd testfiles
for i in $(ls); do
	openssl bf-cfb -in $i -out $i.bf-cfb -k 1
	openssl bf-ofb -in $i -out $i.bf-ofb -k 1
	zip $i.zip $i
	zip $i.bf-cfb $i.zip.bf-cfb
        zip $i.bf-ofb $i.zip.bf-ofb
done	
