const vscode = require('vscode');
const cp = require('child_process');

const output = vscode.window.createOutputChannel('Brian Spiral');
let statusBar;

function exec(command, cb) {
    output.appendLine(`> ${command}`);
    const p = cp.exec(command, (err, stdout, stderr) => {
        if (stdout) output.append(stdout);
        if (stderr) output.append(stderr);
        if (err) {
            vscode.window.showErrorMessage(`${command} failed`);
            statusBar.text = 'Mesh: ✗';
        } else {
            statusBar.text = 'Mesh: ✓';
        }
        cb && cb(err);
    });
    return p;
}

function maybeRunOptimizer(file) {
    if (!file.endsWith('.py')) return;
    if (vscode.workspace.getConfiguration('brian').get('autoOptimizeOnSave')) {
        exec(`brian-optimize ${file}`);
    }
}

function activate(context) {
    statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
    statusBar.text = 'Mesh: -';
    statusBar.show();

    const commands = [
        ['brian.runSelfAudit', () => exec('brian audit --self')],
        ['brian.runBestestBeast', () => exec('tsal-bestest-beast 3')],
        ['brian.optimizeCurrentFile', () => {
            const file = vscode.window.activeTextEditor?.document.fileName;
            if (file) exec(`brian-optimize ${file}`);
        }],
        ['brian.logMeshVectors', () => {
            const file = vscode.window.activeTextEditor?.document.fileName;
            if (file) exec(`tsal-reflect --origin ${file}`);
        }],
    ];

    for (const [name, callback] of commands) {
        const disposable = vscode.commands.registerCommand(name, async () => {
            vscode.window.showInformationMessage(`${name} started`);
            await callback();
            vscode.window.showInformationMessage(`${name} finished`);
        });
        context.subscriptions.push(disposable);
    }

    const saveHook = vscode.workspace.onDidSaveTextDocument(doc => {
        maybeRunOptimizer(doc.fileName);
    });
    context.subscriptions.push(saveHook);
}

function deactivate() {
    output.dispose();
    statusBar.dispose();
}

module.exports = { activate, deactivate };
