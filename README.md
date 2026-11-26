# Franklin Kinetics Labs

The canon and crew for the Labs store on franklinkinetics.com.

## How to use it
- **Labs exist to get owner-led firms to call Brandon.** The plan: `plan/labs-to-calls.md`.
- **Brandon:** read the latest `logs/weekly/` review (under 10 minutes) and clear `QUEUE.md` (under an hour a week). That's all.
- **Claude Code:** open this folder and talk to Ines. She runs the loops in `wiki/loops/` and stops only at the two gates.
- **Claude chat Project:** ask Claude to read this repo before strategy work. Decisions made in chat get recorded in `logs/decisions.md`.

## Map
```
CLAUDE.md            ← crew operating manual (Claude Code loads this)
QUEUE.md             ← everything waiting on Brandon
plan/                ← the current plan and its critique
wiki/loops/          ← every recurring workflow
canon/               ← ontology (incl. the Call Path), guardrails, gates
crew/                ← the four personas (source of truth); retired/ keeps the rest
.claude/agents/      ← thin local wrappers that point to crew/
labs/                ← sparks.md, _template/, one folder per Lab
site/                ← site-wide pages for franklinkinetics.com (e.g. privacy policy)
logs/                ← decisions, gates, friction, weekly/ reviews
models/              ← Living Models and Price Model
rotor/               ← Rotor consulting docs (copies of the Claude Docs masters)
```

## The one rule
If it matters to the crew, it lives here.
