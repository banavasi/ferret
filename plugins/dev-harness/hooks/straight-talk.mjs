// SessionStart hook: inject the straight-talk rules into every session.
// Disable with DEV_HARNESS_STRAIGHT_TALK=0.
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const flag = (process.env.DEV_HARNESS_STRAIGHT_TALK || "").trim().toLowerCase();
if (["0", "false", "off", "no"].includes(flag)) process.exit(0);

const root = process.env.CLAUDE_PLUGIN_ROOT || join(dirname(fileURLToPath(import.meta.url)), "..");

let rules;
try {
  const skill = readFileSync(join(root, "skills", "straight-talk", "SKILL.md"), "utf8");
  // Drop YAML frontmatter; keep the body.
  rules = skill.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "").trim();
} catch {
  process.exit(0);
}

process.stdout.write(
  JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "SessionStart",
      additionalContext: `dev-harness straight-talk mode is ON for this session.\n\n${rules}`,
    },
  }),
);
