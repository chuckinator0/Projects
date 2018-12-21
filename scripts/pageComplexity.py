'''
You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the complexity of the main page of your site.
In order to measure the complexity of the page, you need to find a set of all tags located on the deepest level of a tree correponsing to HTML document. Given a valid HTML
document (which isn't necessarily a valid xhtml document), find all distinct tags located on the deepest level.

Example

For
document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"
the output should be
pageComplexity(document) = ["h1", "p"].

'''

from html.parser import HTMLParser

# Create a subclass of HTMLParser to specify what to do as the parser parses the html
class MyHTMLParser(HTMLParser):
	
	def __init__(self):
		HTMLParser.__init__(self)
		self.depth = 1
		self.max_depth = 0
		self.tags_at_max_depth = set()

	def handle_starttag(self, tag, attrs):
		self.depth += 1
		
		# If we are at the max depth, add the current tag to the set of tags at max depth
		if self.max_depth == self.depth:
			self.tags_at_max_depth.add(tag)
			self.max_depth = self.depth
			
		# If we reach a new max depth, scrap our old set, call this the new max depth, and add the current tag to the set
		elif self.max_depth < self.depth:
			self.max_depth = self.depth
			self.tags_at_max_depth = set([tag])
		

	def handle_endtag(self, tag):
		self.depth -= 1
		
	

def pageComplexity(document):
	
	parser = MyHTMLParser()
	parser.feed(document)
	
	# The problem didn't state it, but we needed to sort the tags lexicographically rather than give them in the order in which they appeared
	return sorted(list(parser.tags_at_max_depth))


document = "<!DOCTYPE html><html><body><h2>Polular russian drinks</h2><ul>  <li>Coffee</li>  <li>Tea    <ul>    <li>Black tea</li>    <li>Green tea      <ul>      <li>China</li>      <li>Africa</li>      </ul>    </li>    </ul>  </li>  <li>Milk</li>  <li>Vodka</li>  <li>Vodka</li>  <li>Vodka</li>  <li>Vodka</li></ul></body></html>"

print(pageComplexity(document)) # should return ['li']