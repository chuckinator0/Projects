'''
You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will
check if the page they are trying to visit is similar to the one in the blacklist.

For that, you've thought of the special algorithm that for two URLs url1 and url2 computes their similarity as following:

Initially their similarity is 0
Then, it is increased by the following rules:
+5, if the same protocol is used in both URLs.
+10, if url1 and url2 have the same address.
+k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
+1 if for each varNames common between them. Additional +1 if the respective values are equal too.
URLs are given in the following format: protocol://address[(/path)*][?query] (where query = varName=value(&varName=value)*, parts given in [] are optional,
and parts in ()* may be repeated several times). Each of the named elements (i.e. protocol, address, path, varName and value) are guaranteed to contain only alphanumeric
characters and periods.

Given the two URLs url1 and url2, compute their similarity using the algorithm described above.

Example

For

url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
and

url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
the output should be
urlSimilarity(url1, url2) = 19.

Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value in both of them.
So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.
'''

from urllib.parse import urlparse

def urlSimilarity(url1, url2):
    
    similarity = 0
    
    url1_parse = urlparse(url1)
    url2_parse = urlparse(url2)
    
    # schema for urlparse:
    # ["protocol", "address", "path", "params", "query", "fragment"]
    
    # check protocol similarity
    if url1_parse[0] == url2_parse[0]: 
        similarity += 5
    
    # check address similarity
    if url1_parse[1] == url2_parse[1]:
        similarity += 10
       
    # calculate path similarity
    def path_similarity_score(path1,path2):
        similarity = 0
        path1_split = path1.split('/') # note the first element of the list is "", followed by path components
        path2_split = path2.split('/')
        for i in range(1,len(path1_split)):
            try:
                if path1_split[i] == path2_split[i]:
                    similarity += 1
                else:
                    break
            except IndexError:
                break
        return similarity
        
    # update similarity score using path similarity
    similarity += path_similarity_score(url1_parse[2], url2_parse[2])
    
    # calculate query similarity
    def query_similarity_score(query1,query2):
        similarity = 0
        
        if not query1 or not query2:
            return 0

        query1_split = query1.split('&')
        query2_split = query2.split('&')

        param_dict = {} # {parameter : value}

        # populate parameter dictionary from query 1
        for equation in query1_split:
            equation = equation.split('=')
            param_dict[equation[0]] = equation[1]

        # compare parameters of query 2 to the parameter dictionary. Increment similarity score if a parameter is in the dictionary.
        # Increment score again if the parameter has the same value as what is in the dictionary.
        for equation in query2_split:
            equation = equation.split('=')
            if equation[0] in param_dict:
                similarity += 1
                if param_dict[equation[0]] == equation[1]:
                    similarity += 1

        return similarity
    
    # update similarity score using query similarity
    similarity += query_similarity_score(url1_parse[4], url2_parse[4])
    
    return similarity


print(urlSimilarity("ftp://www.example.com/query?varName=value","http://example.com/query?varName=value")) # should return 3



