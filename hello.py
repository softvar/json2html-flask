
from flask import json
import ordereddict
import HTMLParser
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

a = ''	

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    checkbox = request.form['users']
    style=""
    print checkbox
    if(checkbox=="1"):
    	style="<table class=\"table table-condensed table-bordered table-hover\""
    else:
    	style="<table border=\"1\""
    #text = {'a':'1','b':'2'}
    jso = '''{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}'''
    #json_input = json.dumps(text)
    try:
        ordered_json = json.loads(text, object_pairs_hook=ordereddict.OrderedDict)
    	#print ordered_json
        processed_text = htmlConvertor(ordered_json,style)
    	#rep(jso)
        global a
        a= ''
        html_parser = HTMLParser.HTMLParser()
        return render_template("my-form.html",	processed_text=html_parser.unescape(processed_text),pro = text)
    except:
    	return render_template("my-form.html",error="Error Parsing JSON!")

def htmlConvertor(ordered_json,style):
		global a
		a=a+ style + "<tr>"
		for k,v in ordered_json.iteritems():
			a=a+ '<th>'+ str(k) +'</th>'
			if(isinstance(v,list)):
				a=a+ '<td><ul>'
				for i in range(0,len(v)):
					a=a+ '<li>'+str(v[i])+'</li>'
				a=a+ '</ul></td>'
				a=a+ '</tr>'
			elif(isinstance(v,unicode)):
				a=a+ '<td>'+ str(v) +'</td>'
				a=a+ '</tr>'
			else:
				a=a+ '<td>'
				a=a+ '<table border="1">'
				htmlConvertor(v,style)
				a=a+ '</table></td>'
		a=a+ '</tr></table>'
		return a

if __name__ == '__main__':
    app.run(debug = True)