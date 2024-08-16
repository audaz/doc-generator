---
creation date: <% tp.file.creation_date() %>
modification date_time: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
modification date: <% tp.file.last_modified_date("YYYY-MM-DD") %>
today: <% tp.date.now("YYYY-MM-DD") %>
---
Mensagem:

<%* tp.user.notice(tp) %>

```dataview table time-played, length, rating from "games" sort rating desc ```



<%*
const dv = app.plugins.plugins.dataview.api; // Dataview Api

let journalThatHappened = dv.pages('"Journaling"').file.name; // Get all journal in folder journaling
let journalCurrentNumber = await journalThatHappened.length; // Get the number of journals
let actualDate = await tp.date.now('YYYY-MM-DD'); // Get the atual date

//await tp.file.rename(`${journalCurrentNumber} ${actualDate}`); // Rename
-%>


2. **Desenvolvedor Tools (Ferramentas para Desenvolvedores)**: Como o Obsidian é um aplicativo baseado em Electron (uma framework que permite o desenvolvimento de aplicativos desktop GUI usando tecnologias web como JavaScript, HTML e CSS), ele herda algumas capacidades de depuração do Chromium/Electron. Em algumas versões ou configurações específicas do Obsidian, você pode ser capaz de acessar as Ferramentas para Desenvolvedores (Developer Tools) do Electron, que incluem um console, inspecionando o aplicativo com `Ctrl+Shift+I` ou `Cmd+Opt+I` em macOS. No entanto, isso depende da versão e das configurações específicas do seu Obsidian e pode não estar disponível para todos os usuários


`Ctrl+Shift+Mensagem:



# <% tp.file.title %>

<% tp.web.daily_quote() %>