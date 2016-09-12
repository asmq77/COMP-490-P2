#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
print "Content-type: text/html"
print
print "<br/>"
print "<center>"
print "<h1>CGI Test </h1>"
print "</center>"
print "<br/>"
print "<h4>Hello ( %s ) Welcom to my page! </h4/>" %(name)
print "<HTML>"
print "<img src=https://s-media-cache-ak0.pinimg.com/236x/05/b8/8b/05b88b160ef2963b35405ac9cd102c4e.jpg>"
print "</img>"
print "<br/>"
print "<form method=get action=https://www.google.com/search>"
print "<label> You can do a Google Search here: <input type=text name=q></label>"
print "<input type=submit value=Submit>"
print "<br/>"
print "</HTML>"