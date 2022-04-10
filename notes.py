


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{{title}} - My ToDo List</title>
#     <!-- title here is a kinda python variable. see controller rendertemplate -->
#     <!-- double braces are for display purpose -->
# </head>
# <body>
#     <h1>My ToDo List</h1>

#     {% for task in all_tasks %}

#         <p>
#             {{task.title}}: <b>  {{ task.description }}</b>
#         </p>

#     {% endfor %}
#     {%%} "sundaes" are for hidden python  