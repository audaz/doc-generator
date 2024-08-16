async function getfilename(tp) {
    const file_aa = tp.file.path() 
    const file_xx = file_aa.replace(/\\\\/g, "\\").replace(/\//g, "\\")
    console.log("title: " + tp.file.title )
    console.log("folder: " + tp.file.folder() )
    console.log("path: " + tp.file.path() )
    "title: " + tp.file.title 
    "folder: " + tp.file.folder() 
    "path: " + tp.file.path() 
}


module.exports = getfilename