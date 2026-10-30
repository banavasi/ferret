// UserPromptSubmit hook: injects a compact ferret router hint on every prompt
// when the user has opted in ($CLAUDE_CONFIG_DIR/.ferret-always).
// Never blocks: any failure exits 0 with no output.

import fs from "node:fs";
import os from "node:os";
import path from "node:path";

try {
  const claudeDir = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude");
  if (!fs.existsSync(path.join(claudeDir, ".ferret-always"))) process.exit(0);

  process.stdout.write(
    "FERRET ROUTER HINT. Classify this prompt: morning|frame|plan|build|debug|browse|" +
      "review|design|quality|ship|save|meta|init|none. If a mode fits: first line " +
      '"Mode: <mode> — <why>", read that section in the ferret skill, run it. Lead with ' +
      "the next action; number steps; restate state; end with one next step. " +
      'If none fits (casual chat, jokes): ignore this hint silently. "normal mode" ' +
      "suspends the harness this session.\n",
  );
} catch {
  process.exit(0);
}
