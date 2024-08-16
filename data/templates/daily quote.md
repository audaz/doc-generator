---
creation date: <% tp.file.creation_date() %>
modification date_time: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
modification date: <% tp.file.last_modified_date("YYYY-MM-DD") %>
today: <% tp.date.now("YYYY-MM-DD") %>
---


# <% tp.file.title %>

<% tp.web.daily_quote() %>
