# Browse — web research that cites sources

Run for how-does-X-work, library comparisons, error messages, docs lookups, and
research questions. The web is evidence, not authority: inspect before you cite.

## 1. Probe capability, then drive

Use whatever this harness offers (search/fetch tools, agent browser, or page fetch).
If only part of the flow is possible (search but no page read), say so once and
work within it. Never hand the user a manual step list for a site without first
offering to drive it yourself.

Authenticated sessions, cookies, and anything that spends money or changes state
need explicit approval first. Read-only public research never waits on permission.

## 2. Source discipline

- **Official docs over blogs.** Primary sources (project docs, specs, changelogs,
  source repos) decide; tutorials and roundups only discover candidates.
- **Inspect, then cite.** A search snippet is not a source. Open the underlying page
  and confirm the claim before it enters an answer, a decision, or code.
- **Cite claims.** Every material external claim carries its URL. No URL, no claim —
  mark it unverified instead of dressing it up.
- **Recency matters.** Record the version or date the claim was true for. APIs move;
  an undated claim is a future bug.

## 3. Capture

- **Quick answers:** cite inline, keep the URLs the user can re-open.
- **Research-shaped questions** (comparisons, evaluations, migrations): write a cited
  findings file in the repo (`docs/research/<slug>.md`): question, sources with URLs,
  what each source supports, recommendation with its evidence, open gaps.
- **Structured extraction** (tables, lists, prices): pull the fields, name the page
  and date, flag anything inferred vs copied.

## 4. Reuse before research

Search the repo and the learnings store first (`sections/save.md`): the answer may
already be captured. A second research pass over settled ground is waste; cite the
stored finding instead.
