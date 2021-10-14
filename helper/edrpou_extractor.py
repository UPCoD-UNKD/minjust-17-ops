# -*- coding: utf-8 -*- 
import HTMLParser
import xml.etree.ElementTree as ET
import pandas as pd 
import html
import codecs
file_path = 'short_UO.xml'
context = ET.iterparse(file_path, events=("start", "end"))
context = iter(context)
event, root = context.__next__()
for event, elem in context:
    if event == "end" and elem.tag == "RECORD":
        value = "зареєстровано"
        #value = u'\u0437'u'\u0430'u'\u0440'u'\u0435'u'\u0454'u'\u0441'u'\u0442'u'\u0440'u'\u043e'u'\u0432'u'\u0430'u'\u043d'u'\u043e'
        if elem[8].text == value:
            NAME = elem[0].text
            SHORT_NAME = elem[1].text
            EDROPOU = elem[2].text
            KVED = elem[4].text
            STAN = elem[8].text
            record = ET.Element('RECORD')
            name = ET.SubElement(record,'NAME')
            name.text = NAME
            short_name = ET.SubElement(record,'SHORT_NAME')
            short_name.text = SHORT_NAME
            edropou = ET.SubElement(record,'EDROPOU')
            edropou.text = EDROPOU
            kved = ET.SubElement(record,'KVED')
            kved.text = KVED
            stan = ET.SubElement(record,'STAN')
            stan.text = STAN
            mydata = ET.tostring(record)
            dataINunicode = mydata.decode("utf-8")
            data_unescape = html.unescape(dataINunicode)
            #dataINunicode = html.parser.HTMLParser().unescape(mydata).encode('utf-8')
            #myfile = open("Active_organisations.xml", "ab")
            #myfile.write(dataINunicode)
            #myfile.write()
            #print(data_unescape)
            root.clear()
            myfile = open("active_organizations.xml", "wb")
            myfile.write(mydata)
            myfile.close()
        root.clear()
    
print('Done!')

file_path = 'active_organizations.xml'
context = ET.iterparse(file_path, events=("start", "end"))
context = iter(context)
event, root = context.next()
for event, elem in context:
    if event == "end" and elem.tag == "RECORD":
        value = u'1'u'5'u'.'u'9'u'8'
        value2 = u'1'u'1'u'.'u'0'u'7'
        value3 = u'1'u'5'u'.'u'3'u'2'
        value4 = u'1'u'0'u'.'u'3'u'2'
        if value in elem[3].text:
            NAME = elem[0].text
            SHORT_NAME = elem[1].text
            EDROPOU = elem[2].text
            KVED = elem[3].text
            STAN = elem[4].text
            record = ET.Element('RECORD')
            name = ET.SubElement(record,'NAME')
            name.text = NAME
            short_name = ET.SubElement(record,'SHORT_NAME')
            short_name.text = SHORT_NAME
            edropou = ET.SubElement(record,'EDROPOU')
            edropou.text = EDROPOU
            kved = ET.SubElement(record,'KVED')
            kved.text = KVED
            stan = ET.SubElement(record,'STAN')
            stan.text = STAN
            mydata = ET.tostring(record)
            dataINunicode = HTMLParser.HTMLParser().unescape(mydata).encode('utf-8')
            myfile = open("group_7.xml", "a")
            myfile.write(dataINunicode)
            root.clear()
        else:
            if value2 in elem[3].text:
                NAME = elem[0].text
                SHORT_NAME = elem[1].text
                EDROPOU = elem[2].text
                KVED = elem[3].text
                STAN = elem[4].text
                record = ET.Element('RECORD')
                name = ET.SubElement(record,'NAME')
                name.text = NAME
                short_name = ET.SubElement(record,'SHORT_NAME')
                short_name.text = SHORT_NAME
                edropou = ET.SubElement(record,'EDROPOU')
                edropou.text = EDROPOU
                kved = ET.SubElement(record,'KVED')
                kved.text = KVED
                stan = ET.SubElement(record,'STAN')
                stan.text = STAN
                mydata = ET.tostring(record)
                dataINunicode = HTMLParser.HTMLParser().unescape(mydata).encode('utf-8')
                myfile = open("group_7.xml", "a")
                myfile.write(dataINunicode)
                root.clear()
            else:
                if value3 in elem[3].text:
                    NAME = elem[0].text
                    SHORT_NAME = elem[1].text
                    EDROPOU = elem[2].text
                    KVED = elem[3].text
                    STAN = elem[4].text
                    record = ET.Element('RECORD')
                    name = ET.SubElement(record,'NAME')
                    name.text = NAME
                    short_name = ET.SubElement(record,'SHORT_NAME')
                    short_name.text = SHORT_NAME
                    edropou = ET.SubElement(record,'EDROPOU')
                    edropou.text = EDROPOU
                    kved = ET.SubElement(record,'KVED')
                    kved.text = KVED
                    stan = ET.SubElement(record,'STAN')
                    stan.text = STAN
                    mydata = ET.tostring(record)
                    dataINunicode = HTMLParser.HTMLParser().unescape(mydata).encode('utf-8')
                    myfile = open("group_7.xml", "a")
                    myfile.write(dataINunicode)
                    root.clear()
                else:
                    if value4 in elem[3].text:
                        NAME = elem[0].text
                        SHORT_NAME = elem[1].text
                        EDROPOU = elem[2].text
                        KVED = elem[3].text
                        STAN = elem[4].text
                        record = ET.Element('RECORD')
                        name = ET.SubElement(record,'NAME')
                        name.text = NAME
                        short_name = ET.SubElement(record,'SHORT_NAME')
                        short_name.text = SHORT_NAME
                        edropou = ET.SubElement(record,'EDROPOU')
                        edropou.text = EDROPOU
                        kved = ET.SubElement(record,'KVED')
                        kved.text = KVED
                        stan = ET.SubElement(record,'STAN')
                        stan.text = STAN
                        mydata = ET.tostring(record)
                        dataINunicode = HTMLParser.HTMLParser().unescape(mydata).encode('utf-8')
                        myfile = open("group_7.xml", "a")
                        myfile.write(dataINunicode)
                        root.clear()
                    else:
                        print(elem[1].text)
            
print('Done!')



xtree = et.parse("group_7.xml")
xroot = xtree.getroot() 


df_cols = ["NAME", "SHORT_NAME", "EDROPOU", "KVED", "STAN"]
rows = []


for node in xroot: 
    s_RECORD = node.attrib.get("RECORD")
    s_NAME = node.find("NAME").text if node is not None else None
    s_SHORT_NAME = node.find("SHORT_NAME").text if node is not None else None
    s_EDROPOU = node.find("EDROPOU").text if node is not None else None
    s_KVED = node.find("KVED").text if node is not None else None
    s_STAN = node.find("STAN").text if node is not None else None
   
    
    
    rows.append({"NAME" : s_NAME, "SHORT_NAME":  s_SHORT_NAME, "EDROPOU": s_EDROPOU, "KVED": s_KVED, "STAN": s_STAN})

out_df = pd.DataFrame(rows, columns = df_cols)
print(out_df)

out_df.to_excel("soda_vater.xls", encoding='cp1251')
