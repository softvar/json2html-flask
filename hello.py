'''
JSON 2 HTML convertor
=====================

(c) Varun Malhotra 2013
Source Code: https://github.com/softvar/json2html
------------

LICENSE: MIT
--------
'''

import ordereddict
import HTMLParser

from flask import json
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
    '''
    receive submitted data and process
    '''
    text = request.form['text']
    checkbox = request.form['users']
    style=""
    if(checkbox=="1"):
    	style="<table class=\"table table-condensed table-bordered table-hover\">"
    else:
    	style="<table border=\"1\">"
    
    #json_input = json.dumps(text)
    try:
        ordered_json = json.loads(text, object_pairs_hook=ordereddict.OrderedDict)
        processed_text = htmlConvertor(ordered_json,style)

        html_parser = HTMLParser.HTMLParser()
        global a
        a = ''
        return render_template("my-form.html",	processed_text=html_parser.unescape(processed_text),pro = text)
    except:
        return render_template("my-form.html",error="Error Parsing JSON!")


def htmlConvertor(ordered_json,style):
		'''
		converts JSON Object into human readable HTML representation
		generating HTML table code with raw/bootstrap styling.
		'''
		global a
		a=a+ style 
		for k,v in ordered_json.iteritems():
			a=a+ '<tr>'
			a=a+ '<th>'+ str(k) +'</th>'
			if(isinstance(v,list)):
				a=a+ '<td><ul>'
				for i in range(0,len(v)):
					if(isinstance(v[i],unicode)):
						a=a+ '<li>'+str(v[i])+'</li>'
					elif(isinstance(v[i],int)):
						a=a+ '<li>'+str(v[i])+'</li>'
					elif(isinstance(v[i],list)==False):
						htmlConvertor(v[i],style)
				a=a+ '</ul></td>'
				a=a+ '</tr>'
			elif(isinstance(v,unicode)):
				a=a+ '<td>'+ str(v) +'</td>'
				a=a+ '</tr>'
			elif(isinstance(v,int)):
				a=a+ '<td>'+ str(v) +'</td>'
				a=a+ '</tr>'
			else:
				a=a+ '<td>'
				#a=a+ '<table border="1">'
				htmlConvertor(v,style)
				a=a+ '</td></tr>'
				#a=a+ '</table></td>'
		a=a+ '</table>'
		return a

if __name__ == '__main__':
    app.run(debug = True)