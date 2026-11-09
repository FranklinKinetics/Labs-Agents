# Franklin Kinetics Labs

The canon and crew for the Labs store on franklinkinetics.com.

## How to use it
- **Claude Code:** open this folder and talk to Ines. "Ines, new Spark: …" or "Ines, where's Automatic Groceries?" She'll run the lifecycle and stop at each gate for you.
- **Claude chat Project:** ask Claude to read this repo before strategy work. Decisions made in chat get recorded in `logs/decisions.md`.

## Map
```
CLAUDE.md            ← crew operating manual (Claude Code loads this)
canon/               ← ontology, guardrails, gates
crew/                ← the seven personas (source of truth)
.claude/agents/      ← thin local wrappers that point to crew/
labs/                ← sparks.md, _template/, one folder per Lab
logs/                ← decisions, gates, friction
models/              ← Living Models and Price Model
rotor/               ← Rotor consulting docs (copies of the Claude Docs masters)
```

## The one rule
If it matters to the crew, it lives here.
