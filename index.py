#coding : utf-8
import cgi
import cgitb

cgitb.enable()
print("Content-type: text/html; charset=utf-8 \n")

html ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">    
     <link rel="stylesheet" href="css/bootstrap.min.css">     
     <link rel="stylesheet" href="css/bootstrap.css">
    <title>Jython</title>
</head>
<body>
    <p class = "text-center">new web page with python and html</p>
    <form method="post" action = "" class = "form-group">
        <div class = "form-group">
            <p><input type="number" name="column" placeholder="column">
            <input type="number" name="row" placeholder="row">
            <input type="submit" id = "Send" value="Send"></p>
        </div>
        
    </form>
"""
print(html)
form = cgi.FieldStorage()


if form.getvalue("row") and form.getvalue("column") :
    row = form.getvalue("row")
    column = form.getvalue("column")
else:
    print(f"erreur de saisi")
    #raise Exception("pseudo non transmitS")
print(f"les lignes et les colonnes sont {row,column} ",row,column)

html  = """
</body>
</html>
"""
print(html)