<%*
const file_aa = tp.file.path() 
//let file_xx = file_aa.replace(/\\/g, "\\\\").replace(/\//g, "\\\\") 
let file_xx = file_aa.replace(/\\/g, "\\").replace(/\//g, "\\") 
file_xx = "\"" + file_xx + "\""
console.log(file_xx) 
output = await tp.user.docgen({file_x: "\"" + file_xx + "\"", b: "value_2"}) 
console.log(output)
%>


....