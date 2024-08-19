<%*
function characterGoal(tp) {
	//Use the Obsidian API to get the CodeMirror Editor
	// const editor = app.workspace.activeLeaf.view.editor;
	// const cursorLine = editor.getCursor().line;

	// //Set the selection in the CodeMirror Editor
	// editor.setSelection({ line: cursorLine, ch: 0 }, { line: cursorLine, ch: 9999 });
	// const id = createBlockHash();
	// const block = `![[${tp.file.title}#^${id}]]`.split("\n").join("");

	let characterGoal = tp.file.content
		.split("\n")
		.filter((line) => line.includes("characterGoal: "))[0]
		.split(": ")[1];

	//Return the selected text and the generated block id
	let charactersDone = tp.file.content.length;

	let charactersLeft = characterGoal - charactersDone;

	let percentage = ((charactersDone / characterGoal) * 100).toFixed(0);

	let notice = `
        Progression
        ${tp.file.content.length} of ${characterGoal}
        ${percentage}%
    `;
	
    console.log(notice);
	new Notice(notice);
	return "";
}

characterGoal(tp);

%>


...