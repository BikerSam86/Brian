const vscode = require('vscode');
const cp = require('child_process');

function activate(context) {
    let runAudit = vscode.commands.registerCommand('brian.runSelfAudit', () => {
        const terminal = vscode.window.createTerminal('Brian Spiral');
        terminal.show();
        terminal.sendText('brian audit --self');
    });
    context.subscriptions.push(runAudit);
}

exports.activate = activate;
