function addBlockRef(tp) {
   
    console.log('Entrando no adbbLOCK')
    //Use the Obsidian API to get the CodeMirror Editor
       const editor = app.workspace.activeLeaf.view.editor
       const cursorLine = editor.getCursor().line
       
    console.log('bla')
    //Set the selection in the CodeMirror Editor
        editor.setSelection({line: cursorLine, ch: 0}, {line: cursorLine, ch: 9999})
    console.log('setSelection')
    const id = createBlockHash();
    let file_x = tp.file.path() 
    
    const block = `![[${tp.file.title}#^${id}]]`.split("\n").join("");
    
    console.log('createdBlockHash')
    // Copy the block reference to the clipboard
    navigator.clipboard.writeText(block).then(text => text);
    
    //Return the selected text and the generated block id
    return tp.file.selection() + `^${id}`.split("\n").join("");
   }
   
   //A simple function to create a random block id
   function createBlockHash() {
    let result = '';
    var characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < 7; i++ ) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
   }
   
   //export the addBlockRef function
   module.exports = addBlockRef