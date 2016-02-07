'''
JSON 2 HTML convertor
=====================

(c) Varun Malhotra 2013
http://softvar.github.io

Source Code: https://github.com/softvar/json2html-flask
------------

LICENSE: MIT
--------
'''
# -*- coding: utf-8 -*-

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
    return render_template("index.html")

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
        print ordered_json
        processed_text = htmlConvertor(ordered_json,style)

        html_parser = HTMLParser.HTMLParser()
        global a
        a = ''
        return render_template("index.html", processed_text=html_parser.unescape(processed_text),pro = text)
    except:
        return render_template("index.html",error="Error Parsing JSON ! Please check your JSON syntax",pro=text)

def iterJson(ordered_json,style):
	global a
	a=a+ style
	for k,v in ordered_json.iteritems():
		a=a+ '<tr>'
		a=a+ '<th>'+ str(k) +'</th>'
		if (v==None):
			v = unicode("")
		if(isinstance(v,list)):
			a=a+ '<td><ul>'
			for i in range(0,len(v)):
				if(isinstance(v[i],unicode)):
					a=a+ '<li>'+unicode(v[i])+'</li>'
				elif(isinstance(v[i],int) or isinstance(v,float)):
					a=a+ '<li>'+str(v[i])+'</li>'
				elif(isinstance(v[i],list)==False):
					iterJson(v[i],style)
			a=a+ '</ul></td>'
			a=a+ '</tr>'
		elif(isinstance(v,unicode)):
			a=a+ '<td>'+ unicode(v) +'</td>'
			a=a+ '</tr>'
		elif(isinstance(v,int) or isinstance(v,float)):
			a=a+ '<td>'+ str(v) +'</td>'
			a=a+ '</tr>'
		else:
			a=a+ '<td>'
			#a=a+ '<table border="1">'
			iterJson(v,style)
			a=a+ '</td></tr>'
	a=a+ '</table>'
def htmlConvertor(ordered_json,style):
	'''
	converts JSON Object into human readable HTML representation
	generating HTML table code with raw/bootstrap styling.
	'''
	global a
	try:
		for k,v in ordered_json.iteritems():
			pass
		iterJson(ordered_json,style)

	except:
		for i in range(0,len(ordered_json)):
			if(isinstance(ordered_json[i],unicode)):
				a=a+ '<li>'+unicode(ordered_json[i])+'</li>'
			elif(isinstance(ordered_json[i],int) or isinstance(ordered_json[i],float)):
				a=a+ '<li>'+str(ordered_json[i])+'</li>'
			elif(isinstance(ordered_json[i],list)==False):
				htmlConvertor(ordered_json[i],style)

	return a

if __name__ == '__main__':
    app.run(debug = True)
