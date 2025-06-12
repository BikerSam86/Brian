# State Tracking

Use `state_log.yaml` to record the evolution of any module.
Each entry stores three fields:

- `WAS_THEN`
- `IS_NOW`
- `WILL_BE`

Update the log via CLI:

```bash
tsal-state tsal.core --was "0.8" --now "1.0" --will "1.1"
```

Before running, `state_log.yaml` looks like:

```yaml
{}
```

After the command:

```yaml
tsal.core:
  WAS_THEN: '0.8'
  IS_NOW: '1.0'
  WILL_BE: '1.1'
```

Display an entry:

```bash
tsal-state tsal.core --show
```

Output:

```yaml
tsal.core:
  WAS_THEN: '0.8'
  IS_NOW: '1.0'
  WILL_BE: '1.1'
```
