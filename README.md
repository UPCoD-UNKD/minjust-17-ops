# minjust-17-ops
Transformation with xml

## Quick solution

```
sed -i -E  's/(\&#[0-9]{1,10};)//gm' 17.1-EX_XML_EDR_UO_FULL.xml
xmllint --noout --stream --schema 17.1-EX_XML_EDR_UO_FULL.xsd 17.1-EX_XML_EDR_UO_FULL.xml
```

This is clean and verify XML

### TODO
Create base CSV from XML - https://pragmaticintegrator.wordpress.com/2012/10/28/transforming-xml-to-csv-via-xslt/



