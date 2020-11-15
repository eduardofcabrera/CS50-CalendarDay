Welcome to Calendar.

Calender is a self calendar that help us to organize our lifes. We can set appointments, advices and tasks that we need to do, and with a good interface, calendar shows us ours needs. In each object_TAA (the way that I called appointments, advices and tasks in the projects) we can set a content, priority, date created, date finish, weekly routine, days of the week and if is active, all of theses will be show up in the responsive and clean interface made with JS. I hope that you like! Sorry if has some english errors, I'm from Brazil, it's a pleasure to make CS50 Web! Thank you!

In the main directory of CalendarDay has 3 folders: vscode(I used VSCode so is just the config for python), CalendarDay(the main folder of django project with the standarts files of django) and de day_day(the name of the app).

In the day_day folder has the standarts django's files and folders(__pycache__ and __init__.py) that I did not change.
    Migrations: has the history of migrations that I used in the project(can see the models in models.py).
    Static/day_day: has the .css, static.css of the first page and staticLayout.css of the main user page, and .js files, index_log_out.js of the first page and layout.js of the main user page.
    Templates/calendarDay: has the .html files, index_log_out.html and mid-log-out.html of the first page and layout.html of the main user page.
    admin.py: I registered the models in the admin site.
    apps.py: is the day_day app installed.
    get.py: All basic functions of the backend is there, I tried to clean the most of I can the views.py.
    models.py: has the models that I utilized.
    tests.py: has the tests of get.py.
    urls.py: has the urls of views and front-end api's.
        API's that I used fetch in JS:
            path('TAA/<str:type_TAA>/<int:TAA_id>', views.TAA_API, name='TAA_API'),
            path('active/<str:type_TAA>/<int:TAA_id>', views.activeUnactive, name='activeAPI'),
            path('edit/<str:type_TAA>/<int:TAA_id>', views.editTAA, name='editAPI'),
            path('delete/<str:type_TAA>/<int:TAA_id>', views.deleteTAA, name='deleteAPI')
    views.py: has the mains bacends functions.

Requirements:
    My final project is a calendar for self use, what have a huge difference between the others projects in the course;
    My project utilize django on the back-end, like we can see in the django files, and JavaScript on the front-end, like we see in the static folder, in the files index_log_out.js and layout.js.
    My project is mobile responsive, we can see that in the css's files, static.css and staticLayout.css, that in the bottom we have the @media to make a good responsive design. But we can see in the video demonstration too.

* I tried to make a clean code, but in some times I could not, in the JS files it's a little bit messy. I hope that you liked. Thank you! 
    