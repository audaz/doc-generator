<%*
new Notice('gerando documento...')
const file_aa = tp.file.path() 
//let file_xx = file_aa.replace(/\\/g, "\\\\").replace(/\//g, "\\\\") 
let file_xx = file_aa.replace(/\\/g, "\\").replace(/\//g, "\\") 
file_xx = "\"" + file_xx + "\""
//let arguments = {file_x: "\"" + file_xx + "\"", empresa: "nikos"}
let arguments = {file_x: "\"" + file_xx + "\"", empresa: 'audaz'}
console.log(file_xx) 
console.log(arguments)
//output = await tp.user.docgen({file_x: "\"" + file_xx + "\"", empresa: "nikos"}) 
output = await tp.user.docgen(arguments)
console.log(output)
new Notice('documento gerado...')
%>