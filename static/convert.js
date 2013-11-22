

function process() {
        document.getElementById('table').style.display = "none";
    }

processed_data = document.getElementById('table').innerHTML;
    	if(processed_data){
    		convertHtmlToText();
    	}

function convertHtmlToText() {

    var inputText = document.getElementById("table").innerHTML;
    var returnText = "" + inputText;

    //-- remove BR tags and replace them with line break
    returnText=returnText.replace(/<br>/gi, "\n");
    returnText=returnText.replace(/<br\s\/>/gi, "\n");
    returnText=returnText.replace(/<br\/>/gi, "\n");

    //-- remove P and A tags but preserve what's inside of them
    returnText=returnText.replace(/<p.*>/gi, "\n");
    returnText=returnText.replace(/<a.*href="(.*?)".*>(.*?)<\/a>/gi, " $2 ($1)");

    //-- remove all inside SCRIPT and STYLE tags
    returnText=returnText.replace(/<script.*>[\w\W]{1,}(.*?)[\w\W]{1,}<\/script>/gi, "");
    returnText=returnText.replace(/<style.*>[\w\W]{1,}(.*?)[\w\W]{1,}<\/style>/gi, "");
    //-- remove all else
    returnText=returnText.replace(/<(?:.|\s)*?>/g, "");

    //-- get rid of more than 2 multiple line breaks:
    returnText=returnText.replace(/(?:(?:\r\n|\r|\n)\s*){2,}/gim, "\n\n");

    //-- get rid of more than 2 spaces:
    returnText = returnText.replace(/ +(?= )/g,'');

    //-- get rid of html-encoded characters:
    returnText=returnText.replace(/&nbsp;/gi," ");
    returnText=returnText.replace(/&amp;/gi,"&");
    returnText=returnText.replace(/&quot;/gi,'"');
    returnText=returnText.replace(/&lt;/gi,'<');
    returnText=returnText.replace(/&gt;/gi,'>');

    //-- return
    document.getElementById("outputTable").innerHTML = returnText;
    if(document.getElementById('outputTable').innerHTML!="")
        window.location.hash = "sendButton";
    if(returnText!=null)
    document.getElementById("output").value = returnText;
    
}
