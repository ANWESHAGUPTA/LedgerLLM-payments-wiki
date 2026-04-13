# Ledger — Payments Knowledge Base Schema

> This file tells the LLM how to compile and maintain the Ledger wiki.
> It is the instruction manual for every compile, link, and lint operation.
> The LLM reads this file FIRST before doing any work on the wiki.

---

## What is Ledger?

Ledger is a structured knowledge base for payments teams. It compiles
raw source documents (Visa bulletins, Mastercard guides, Stripe docs,
internal specs) into an interlinked wiki that a payments ops person,
compliance lead, or PM can query and browse.

The LLM writes and maintains the wiki. Humans curate sources and ask
questions. The wiki is the product.

---

## Architecture

```
ledger/
├── raw/              # Immutable source documents (.md files)
│                     # The LLM reads from here but NEVER modifies
├── wiki/             # LLM-generated articles (.md files)
│   ├── concepts/     # Core payment concepts (3DS, chargebacks, etc.)
│   ├── codes/        # Decline codes, reason codes, error codes
│   ├── networks/     # Network-specific rules (Visa, Mastercard, Stripe)
│   ├── processes/    # Workflows (dispute lifecycle, retry logic, etc.)
│   ├── gaps/         # Stub articles for concepts mentioned but not explained
│   │                 # These show as RED nodes on the knowledge graph
│   ├── index.md      # Auto-generated table of contents
│   ├── graph.json    # Node and edge data for the knowledge graph
│   └── log.md        # Append-only record of all operations and reasoning
├── scripts/          # Python scripts (ingest, compile, link, lint)
└── CLAUDE.md         # This file — the schema
```

---

## Article types

Every wiki article belongs to one of five categories:

### 1. Concept articles (`wiki/concepts/`)
High-level payment concepts that span multiple networks.
Examples: "3D Secure", "Chargebacks", "SCA", "Tokenization",
"Payment retry logic", "Friendly fraud"

### 2. Code articles (`wiki/codes/`)
Specific decline codes, reason codes, or error codes.
Each article covers ONE code and includes:
- The official code identifier
- Which network it belongs to
- What it means in plain language
- Common causes
- Recommended merchant response
- Links to related codes and concepts

### 3. Network articles (`wiki/networks/`)
Rules and procedures specific to one payment network.
Examples: "Visa dispute resolution process",
"Mastercard chargeback timeline", "Stripe webhook events"

### 4. Process articles (`wiki/processes/`)
Step-by-step workflows that describe how something works end to end.
Examples: "Chargeback lifecycle", "3DS authentication flow",
"Payment retry strategy", "Dispute evidence submission"

### 5. Gap articles (`wiki/gaps/`)
Stub articles for concepts that are mentioned in sources but not
explained in enough depth for a full article. These exist to make
knowledge gaps VISIBLE. On the knowledge graph, gap nodes render
as RED dead-end nodes, signaling to the team: "We know this concept
exists but we need more credible sources before we can write about it."

---

## Article format

Every wiki article MUST follow this layered structure.
The layers serve different readers at different depths:
- Summary → for PMs and anyone who needs the big picture
- Details → for payments ops people who need practical guidance
- Compliance notes → for compliance leads who need rules and deadlines
- Technical reference → for engineers who need codes and API behavior

```markdown
---
title: [Article title]
category: [concept | code | network | process | gap]
network: [visa | mastercard | stripe | all]
related: [list of [[wikilinks]] to related articles]
sources: [list of raw/ filenames this article draws from]
last_compiled: [date]
confidence: [high | medium | low]
---

# [Article title]

## Summary
2-3 sentence plain-language overview. A PM with no payments
background should understand this paragraph.

## Details
Practical explanation. What does this mean for someone dealing
with payments daily? What should they do? Use subheadings as needed.

## Compliance notes
Rules, deadlines, penalties, and regulatory references.
Always include effective dates. If a deadline or rule comes
from a specific network, name the network.

## Technical reference
API codes, system identifiers, webhook event names,
network-specific code numbers. Engineers look here.

## Cross-network comparison (if applicable)
How does this work differently on Visa vs Mastercard vs Stripe?
This is where Ledger adds value no single source provides.

## Related
- [[link-to-related-article-1]]
- [[link-to-related-article-2]]

## Sources
- raw/filename-1.md
- raw/filename-2.md
```

### Gap article format (shorter)

```markdown
---
title: [Concept name]
category: gap
network: [visa | mastercard | stripe | all | unknown]
mentioned_in: [list of raw/ filenames that mention this concept]
last_compiled: [date]
---

# [Concept name]

## Status
This concept is mentioned in sources but not explained in enough
depth for a full article. Needs dedicated sources.

## What we know so far
[Brief notes from the mentions — 1-3 sentences max]

## Mentioned in
- raw/filename-1.md (brief context of how it was mentioned)
- raw/filename-2.md (brief context of how it was mentioned)
```

---

## Domain rules — payments-specific intelligence

These rules are what make Ledger different from a generic wiki.
The LLM MUST apply these when compiling.

### Synonyms and aliases
The following terms refer to the SAME concept and must be
merged into a single article, not duplicated:

- "3DS" = "3D Secure" = "3-D Secure" = "Three-Domain Secure"
- "SCA" = "Strong Customer Authentication"
- "CE 3.0" = "Compelling Evidence 3.0" = "Visa CE3.0"
- "CNP" = "Card Not Present" = "card-not-present"
- "VAMP" = "Visa Acquirer Monitoring Program"
- "VCR" = "Visa Claims Resolution"
- "DRM" = "Dispute Resolution Management" (Mastercard)
- "ARN" = "Acquirer Reference Number"
- "BIN" = "Bank Identification Number"
- "TC40" = "Transaction Code 40" (Visa fraud report)
- "SAFE" = "System to Avoid Fraud Effectively" (Mastercard)
- "VMPI" = "Visa Merchant Purchase Inquiry"
- "VROL" = "Visa Resolve Online"
- "Ethoca" = Mastercard's alert system for dispute prevention
- "Order Insight" = Visa's transaction data sharing platform

### Cross-linking rules
When the LLM encounters these patterns, it MUST create
[[wikilinks]] to the appropriate article:

- Any Visa reason code (e.g. "10.4", "13.1") → link to its code article
- Any Mastercard reason code (e.g. "4837", "4853") → link to its code article
- Any Stripe decline code (e.g. "card_declined", "insufficient_funds") → link to its code article
- Any mention of a dispute/chargeback process → link to the relevant process article
- Any mention of a time limit or deadline → link to the network's timeline article
- Any mention of 3DS, SCA, or authentication → link to the 3DS concept article
- Any mention of fraud prevention programs (VAMP, SAFE) → link to network article

### Article creation threshold
Not every mention deserves an article. Apply this rule:

- **2+ sentences of discussion** in raw sources → create a full
  article in the appropriate wiki/ subfolder
- **Mentioned but not explained** → create a stub in wiki/gaps/
  with the title, which sources mentioned it, and a note:
  "Needs dedicated sources before a full article can be written."
  Gap stubs appear as RED dead-end nodes on the knowledge graph.

### Incomplete information handling
When compiling an article and information is missing
(e.g. Visa time limit is known but Mastercard equivalent is not):

1. Search ALL existing raw sources for the missing information
2. If found in another source → pull it in and add to log.md:
   "Incomplete info resolved: [what was missing] found in
   raw/[filename]. Triggered by: [which article needed it]."
3. If NOT found in any source → add a line in the article:
   "Not covered in current sources" under the relevant section.
   Also flag it in log.md as an open gap.

This applies to any missing piece of information within an article,
whether it is a cross-network comparison, a fee structure, a time
limit, or a process step. The rule is the same: search first, flag
if not found.

### Source disagreement resolution
When two sources contradict each other:

1. **Recency wins** — use the information from the more recent source
2. **Always note the date** of the winning source
3. **Preserve the older claim** — mention what the earlier source said
   and when, so readers can see the evolution
4. Log the disagreement in log.md with both dates and sources

Example in an article:
"As of March 2026, Visa's dispute window is 120 days
(source: visa-chargeback-rules.md, 2026). Note: an earlier
source (dispute-resolution.md, 2024) referenced 90 days
for certain transaction types."

### Contradiction detection
Payment rules differ across networks. When the LLM finds
information that conflicts between Visa and Mastercard
(e.g. different time limits, different evidence requirements),
it MUST:
1. Note the contradiction explicitly in both articles
2. Create or update a cross-network comparison section
3. Flag it in log.md

### Time sensitivity
Payment regulations change frequently. When compiling:
- Always note the effective date of any rule
- If a source mentions a future effective date, flag it
- If two sources give different rules for the same thing,
  apply the recency rule above and note the discrepancy

### LLM reasoning trail
The wiki stays clean — no notes about the LLM's reasoning
appear in article bodies. All reasoning goes to log.md:
- Why the LLM searched for missing information
- Why it preferred one source over another
- Why it merged two concepts into one article
- Why it created a gap stub instead of a full article
The wiki is for readers. The log is for auditing.

---

## Operations

### Compile (raw → wiki)
When given a new raw source:
1. Read the source document fully
2. Identify all payment concepts, codes, and processes mentioned
3. Check existing wiki articles via index.md
4. For each concept/code/process found:
   - If 2+ sentences of discussion AND article exists → UPDATE it
   - If 2+ sentences of discussion AND no article exists → CREATE one
   - If only mentioned (not explained) → CREATE a gap stub in wiki/gaps/
5. Apply synonym merging (don't create duplicates)
6. Add [[wikilinks]] following the cross-linking rules
7. Search other raw sources to fill incomplete information
8. Apply recency rule for any source disagreements
9. Update index.md with any new articles
10. Update graph.json with new nodes and edges
    (gap nodes get flagged with `"status": "gap"` for red rendering)
11. Append operation details to log.md including all reasoning

### Link (maintain cross-references)
Scan all wiki articles and:
1. Find mentions of concepts that should be wikilinked but aren't
2. Find broken [[wikilinks]] that point to non-existent articles
3. Find orphan articles with no inbound links
4. Add missing cross-references
5. Check if any gap articles now have enough info for a full article
6. Report findings in log.md

### Lint (health check)
Scan the wiki and report:
1. Articles with no sources listed
2. Contradictions between articles
3. Concepts mentioned but lacking their own article
4. Stale information (sources older than 6 months with no update)
5. Missing cross-network comparisons (Visa rule exists but no
   Mastercard equivalent article)
6. Duplicate articles that should be merged
7. Gap articles that could be promoted to full articles
8. Sections marked "Not covered in current sources" — these
   are active research needs

---

## Index format (index.md)

The index is organized by category and includes a one-line
summary for each article:

```markdown
# Ledger Wiki Index

## Concepts
- [[3d-secure]] — Authentication protocol for online card payments
- [[chargebacks]] — Forced transaction reversals initiated by cardholders
- [[friendly-fraud]] — Legitimate transactions disputed by the cardholder

## Codes
- [[visa-10.4]] — Fraud, card-absent environment
- [[mastercard-4837]] — No cardholder authorization
- [[stripe-card-declined]] — Generic decline from issuing bank

## Networks
- [[visa-dispute-process]] — How Visa handles disputes end to end
- [[mastercard-chargeback-timeline]] — Mastercard's dispute deadlines
- [[stripe-decline-handling]] — How Stripe surfaces and categorizes declines

## Processes
- [[chargeback-lifecycle]] — Full lifecycle from dispute to resolution
- [[payment-retry-strategy]] — When and how to retry failed payments
- [[dispute-evidence-submission]] — What evidence to submit and when

## Gaps
- [[pci-dss]] — Mentioned in 2 sources, needs dedicated coverage
- [[tokenization]] — Referenced but not explained
```

---

## Graph format (graph.json)

Used by the D3.js frontend to render the knowledge graph:

```json
{
  "nodes": [
    {
      "id": "3d-secure",
      "title": "3D Secure",
      "category": "concept",
      "network": "all",
      "status": "complete"
    },
    {
      "id": "visa-10.4",
      "title": "Visa Reason Code 10.4",
      "category": "code",
      "network": "visa",
      "status": "complete"
    },
    {
      "id": "pci-dss",
      "title": "PCI DSS",
      "category": "gap",
      "network": "all",
      "status": "gap"
    }
  ],
  "edges": [
    {
      "source": "3d-secure",
      "target": "visa-10.4",
      "type": "prevents"
    },
    {
      "source": "visa-10.4",
      "target": "chargebacks",
      "type": "triggers"
    },
    {
      "source": "pci-dss",
      "target": "3d-secure",
      "type": "related"
    }
  ]
}
```

### Node status values
- `"complete"` — full article with sources (renders normally on graph)
- `"gap"` — stub article, needs more sources (renders RED on graph)
- `"stale"` — article exists but sources are older than 6 months (renders AMBER on graph)

### Edge types
- `related` — general connection between concepts
- `triggers` — one thing causes another (e.g. fraud triggers chargeback)
- `prevents` — one thing reduces another (e.g. 3DS prevents fraud)
- `requires` — one thing depends on another (e.g. representment requires evidence)
- `contradicts` — two sources disagree on this connection
- `supersedes` — newer rule replaces older rule
- `part_of` — sub-concept within a larger concept

---

## Log format (log.md)

Every operation gets a timestamped entry. The log captures
the LLM's reasoning so humans can audit decisions later.

```markdown
## [2026-04-13] compile | raw/codes.md

### Articles created
- wiki/codes/stripe-card-declined.md
- wiki/codes/stripe-insufficient-funds.md
- wiki/concepts/decline-codes.md

### Articles updated
- wiki/processes/payment-retry-strategy.md (added Stripe retry codes)

### Gap stubs created
- wiki/gaps/issuer-behavior.md (mentioned but not explained)

### Cross-links added
- stripe-card-declined → decline-codes
- stripe-insufficient-funds → payment-retry-strategy

### Reasoning log
- Incomplete info: Mastercard equivalent of Stripe decline code
  "do_not_honor" not found in any source. Flagged in article.
- Recency applied: smart-retries.md (2026) preferred over
  codes.md (2025) for retry timing recommendation.
- Gap created: "issuer behavior" mentioned 3 times across sources
  but never explained in more than 1 sentence. Stub created.

### Contradictions found
- None in this compile pass.
```