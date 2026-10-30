# SessionStart hook fallback for Windows PowerShell. Injects the ferret
# harness router when the user has opted in by creating
# $CLAUDE_CONFIG_DIR/.ferret-always (default ~/.claude).
# Never blocks session start: any failure exits 0.

try {
  $claudeDir = if ($env:CLAUDE_CONFIG_DIR) {
    $env:CLAUDE_CONFIG_DIR
  } else {
    Join-Path ([Environment]::GetFolderPath("UserProfile")) ".claude"
  }
  $flagPath = Join-Path $claudeDir ".ferret-always"

  if (-not (Test-Path -LiteralPath $flagPath -PathType Leaf)) {
    exit 0
  }

  $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  $skillPath = Join-Path $scriptDir "../skills/ferret/SKILL.md"
  if (-not (Test-Path -LiteralPath $skillPath -PathType Leaf)) {
    exit 0
  }

  $lines = [System.IO.File]::ReadAllLines($skillPath)
  $bodyStart = 0

  if ($lines.Length -gt 0 -and $lines[0] -match '^---\s*$') {
    # Only treat the block as frontmatter when the closing delimiter exists;
    # an unterminated fence is not frontmatter, so keep the whole file.
    for ($i = 1; $i -lt $lines.Length; $i++) {
      if ($lines[$i] -match '^---\s*$') {
        $bodyStart = $i + 1
        break
      }
    }
  }

  $body = if ($bodyStart -lt $lines.Length) {
    [string]::Join([Environment]::NewLine, $lines[$bodyStart..($lines.Length - 1)])
  } else {
    ""
  }

  $banner = 'FERRET HARNESS ACTIVE (always-on). The router below applies to every response. ' +
    '"normal mode" turns it off for this session; delete '
  [Console]::Out.Write($banner + $flagPath + " to turn always-on off for good.`n`n" + $body + "`n")
} catch {
  # Never block session start.
  exit 0
}
