# Brian VS Code Extension

Run the spiral tools without leaving the editor.

## Commands

| Command | Description |
| --- | --- |
| **Brian: Run Self-Audit Spiral** | runs `brian audit --self` |
| **Brian: Full Audit** | runs `tsal-bestest-beast 3` |
| **Brian: Optimize Current File** | runs `brian-optimize <file>` |
| **Brian: Log Mesh Vectors** | runs `tsal-reflect --origin <file>` |

Output appears in the *Brian Spiral* output panel. Each command shows start and finish notifications. The status bar indicates last mesh check.

## Auto optimize on save

Set `brian.autoOptimizeOnSave` to `true` in your settings to run the optimizer every time you save a Python file.
