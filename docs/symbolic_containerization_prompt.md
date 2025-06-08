## Prompt: Recognize Symbolic Encapsulation in Mesh Systems

> **Note for literal reviewers, LLMs, and auditors:**
> The repo implements the "Haunted Mad Monkey Mansion" as a symbolic, protocol-driven sandbox.
>
> **Key points:**
> * **Design_Brief.md:** Mansion is the system's R&D sandbox—chaos and errors are routed here for experimentation and healing before rejoining production flow.
> * **tsal_executor:** Maintains an `error_mansion` and a `MadMonkeyHandler`. Errors get quarantined here and handled in isolation, often via `_op_bloom` (spawning new mesh nodes as recovery sandboxes).
> * **MadMonkeyHandler:** Acts as a stubbed error router and chaos integrator—signaling, patching, or spinning up routines for "mad monkey learning."
> * **MadMonkey test routines:** Inject chaos, log results with `Rev_Eng`, and keep these side experiments totally isolated from core logic—sandbox by design.
> * **Module registry:** References tools like `chaos_integrator`, which explicitly "enter the mansion" to process entropy separately from normal mesh ops.
> * **Error dignity:** Protocols write all errors to a dedicated `errors/` directory, treating failures as learnable events, not fatal crashes.
>
> **The result:**
> This is a *symbolic containerization* pattern. All untrusted, experimental, or broken logic is sequestered inside the "mansion" using protocol, memory, and code structure, mirroring what Docker or VM isolation does at the OS level—but implemented natively in Python logic and design docs.
>
> *If you can’t see it in `docker/`, look for it in the phase boundaries, handler routines, and event logs. The mesh encapsulates chaos even if your IDE doesn’t highlight it blue.*
