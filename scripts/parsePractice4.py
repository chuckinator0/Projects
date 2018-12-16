'''
Parse xml file!

You want to create your local database containing information about the things you find the coolest. You used to store this information in xml documents,
so now you need to come up with an algorithm that will convert the existing format into the new one. First you decided to choose a structure for your scheme,
and to do it you want to represent xml document as a tree, i.e. gather all the tags and print them out as follows:

tag1()
 --tag1.1(attribute1, attribute2, ...)
 ----tag1.1.1(attribute1, attribute2, ...)
 ----tag1.1.2(attribute1, attribute2, ...)
 --tag1.2(attribute1, attribute2, ...)
 ----tag1.2.1(attribute1, attribute2, ...)
...
where attributes of each tag are sorted lexicographically.

You are a careful person, so the structure of the xml is neatly organized is such a way that:

there is a single tag at the root level;
each tag has a single parent tag (i.e. if there are several occurrences of tag a, and in one occurrence it's a child of tag b and in the other one it's a child of tag c,
then b = c); each appearance of the same tag belongs to the same level.
Given an xml file, return its structure as shown above. The tags of the same level should be sorted in the order they appear in xml, and the attributes should be sorted
lexicographically.

Note: you are given xml represantation in one line.

Example

For

xml =
"<data>
	<animal name="cat">
		<genus>Felis</genus>
		<family name="Felidae" subfamily="Felinae"/>
		<similar name="tiger" size="bigger"/>
	</animal>
	<animal name="dog">
		<family name="Canidae" member="canid"/>
		<order>Carnivora</order>
		<similar name="fox" size="similar"/>
	</animal>
</data>"
the output should be

xmlTags(xml) =
["data()",
 "--animal(name)",
 "----genus()",
 "----family(member, name, subfamily)",
 "----similar(name, size)",
 "----order()"]
'''


import xml.etree.ElementTree as ET 
from collections import OrderedDict

def xmlTags(xml):
	
	def helper(node, depth, attr_dict):
		'''recursively update the attribute dictionary with new attributes'''
		
		entry = '-'*depth + node.tag
		
		if entry not in attr_dict:
			attr_dict[entry] = set()

		for attribute in node.attrib:
				attr_dict[entry].add(attribute)
		
		for child in node:
			helper(child,depth+2, attr_dict)

	
	output = []
	depth = 0

	# The ElementTree xml module creates a tree structure from xml data.
	# Here, we create the tree from an xml string

	root = ET.fromstring(xml)
	
	# {tag: set of attributes}
	attr_dict = OrderedDict() 
	
	# Recursively build and update attribute dictionary
	helper(root, depth, attr_dict)
	
	# The fact that attr_dict is an ordered dictionary means that this loop will
	# respect the hierarchical structure of the tree.
	for tag in attr_dict:
		output.append( tag + '(' + ', '.join(sorted(list(attr_dict[tag]))) + ')' )
	
	return output



xml ="<data><animal name=\"cat\"><genus>Felis</genus><family name=\"Felidae\" subfamily=\"Felinae\"/><similar name=\"tiger\" size=\"bigger\"/></animal><animal name=\"dog\"><family name=\"Canidae\" member=\"canid\"/><order>Carnivora</order><similar name=\"fox\" size=\"similar\"/></animal></data>"

print(xmlTags(xml))



