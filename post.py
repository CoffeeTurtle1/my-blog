#!/usr/bin/python
import sys
from datetime import date
import markdown

html_header = """<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <meta http-equiv="X-UA-Compatible" content="ie=edge"> <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"> <link rel="stylesheet" href="../styles.css"> <script src="../main.js"></script> <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script> <title>Joe Legg</title> </head> <body> <div id="main"> <button style="float: left;" id="darkmode" onclick="dark()">Dark Mode</button></p> <ul> <li><a href="../about.html">About</a></li> <li>|</li> <li><a href="../blog.html">Blog</a></li> <li>|</li> <li><a href="../index.html">Home</a></li> </ul> <div id="blogpostcontainer">"""

html_footer = """</div> <div id='disqus_thread'></div> <script> (function() { var d = document, s = d.createElement('script'); s.src = 'https://joescomputerblog.disqus.com/embed.js'; s.setAttribute('data-timestamp', +new Date()); (d.head || d.body).appendChild(s); })(); </script> <noscript>Please enable JavaScript to view the <a href='https://disqus.com/?ref_noscript'>comments powered by Disqus.</a></noscript> <footer> <p style='margin-top: 40px; font-size: 16px; color: #547aa1;'>© Joe Legg 2019</p> </footer> </div> </body> <script id='dsq-count-scr' src='//joescomputerblog.disqus.com/count.js' async></script> </html>"""

def md_file_to_html(markdown_filename):
    f = open(markdown_filename, "r")
    md = markdown.Markdown()
    html = md.convert(f.read())
    f.close()
    return html_header + html + html_footer

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        print("Creating new post...")

        if (args[0][-2:] != "md"):
            print("Must input a markdown file.")
            exit(1)

        html = md_file_to_html(args[0])

        output_file = open(args[0][:-3] + ".html", "w")
        output_file.write(html)
        output_file.close()

        post_list_f = open("blog.html", "r+")
        post_list = post_list_f.readlines()
        post_list_f.close()

        if input("Is this a new post? [y/n]") == "y":
            title = input("Title: ")
            description = input("Description: ")
            date_str = date.today().strftime("%d %m %Y")

            post_list.insert(30, '<a href="' + args[0][:-3] + '.html">' +
                             title + '</a><small class="post">' + date_str +
                             '</small><p>' + description + '</p><hr>')

            post_list_f = open("blog.html", "w")
            post_list_f.writelines(post_list)
            post_list_f.close()
        print("Done.")
    else:
        print("Invalid number of arguments.")

main()
