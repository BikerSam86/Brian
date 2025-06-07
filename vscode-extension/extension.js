const vscode = require('vscode');
const cp = require('child_process');

function runInTerminal(command) {
    const terminal = vscode.window.createTerminal('Brian Spiral');
    terminal.show();
    terminal.sendText(command);
}

function activate(context) {
    const commands = [
        ['brian.runSelfAudit', () => runInTerminal('brian audit --self')],
        ['brian.runBestestBeast', () => runInTerminal('tsal-bestest-beast 3')],
        ['brian.optimizeCurrentFile', () => {
            const file = vscode.window.activeTextEditor?.document.fileName;
            if (file) runInTerminal(`brian-optimize ${file}`);
        }],
        ['brian.logMeshVectors', () => {
            const file = vscode.window.activeTextEditor?.document.fileName;
            if (file) runInTerminal(`tsal-reflect --origin ${file}`);
        }],
    ];

    for (const [name, callback] of commands) {
        const disposable = vscode.commands.registerCommand(name, callback);
        context.subscriptions.push(disposable);
    }
}

exports.activate = activate;
