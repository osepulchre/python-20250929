from lxml import etree

source_file="livres.xml"
target_file="livres2.xml"

xsl_file="style.xsl"

source_xml = etree.parse(source_file)
xslt   = etree.parse(xsl_file)
transformer = etree.XSLT(xslt)

result = transformer(source_xml)

with open(target_file, "wb") as f:
    f.write(etree.tostring(
        result,                       
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8"
    ))
