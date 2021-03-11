#coding:utf-8
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("row") and form.getvalue("column") :
    row = form.getvalue("row")
    column = form.getvalue("column")
else:
    raise Exception("pseudo non transmitS")


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
"""
print(html)

print(f"les lignes et les colonnes sont {row,column} ",row,column)
html = """
 <form action="/action_page.php">
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <div class="checkbox">
    <label><input type="checkbox"> Remember me</label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form> 
</body>
</html>
"""
print(html)

#column = from.getvalue("column")
#print(f"les colonnes sont {column}")