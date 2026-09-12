# Backup retention cleanup — SDAIA Academy workspace — 12 September 2026
# Policy: keep the current generation + the 2 newest + the last August anchor (2026-08-30c).
# This script MOVES over-retention backups into _cleanup_2026-09-12\ (it does not delete).
# Review that folder, then delete it yourself when you are satisfied.
$ErrorActionPreference = 'Stop'
$Root = 'C:\Users\enezi\Claude\Projects\Academy'
$Dest = Join-Path $Root '_cleanup_2026-09-12'
New-Item -ItemType Directory -Force -Path $Dest | Out-Null

$Files = @(
 'index.backup-2026-09-05g.html',
 'index.backup-2026-09-05h.html',
 'index.backup-2026-09-05i.html',
 'Graduates\Graduates_Database.backup-2026-09-05g.md',
 'Graduates\Graduates_Database.backup-2026-09-05g.xlsx',
 'Graduates\Graduates_Database.backup-2026-09-05h.md',
 'Graduates\Graduates_Database.backup-2026-09-05h.xlsx',
 'Graduates\Graduates_Database.backup-2026-09-05j.md',
 'Graduates\Graduates_Database.backup-2026-09-05j.xlsx',
 'Graduates\index.backup-2026-09-05g.html',
 'Graduates\index.backup-2026-09-05h.html',
 'Graduates\index.backup-2026-09-05i.html',
 'Graduates\index.backup-2026-09-05j.html',
 'SuccessStories\website\js\data.backup-2026-09-05i.js',
 'SuccessStories\website\js\data.backup-2026-09-05j.js',
 'SuccessStories\website\js\data.backup-2026-09-08b.js',
 'SuccessStories\website\sdaia-success-stories-standalone.backup-2026-09-05i.html',
 'SuccessStories\website\sdaia-success-stories-standalone.backup-2026-09-05j.html',
 'SuccessStories\website\sdaia-success-stories-standalone.backup-2026-09-08b.html'
)

$moved = 0; $skipped = 0; $bytes = 0
foreach ($rel in $Files) {
    $src = Join-Path $Root $rel
    if (Test-Path $src) {
        $leaf = Split-Path $rel -Leaf
        $target = Join-Path $Dest $leaf
        $i = 1
        while (Test-Path $target) { $target = Join-Path $Dest ("{0}.{1}" -f $leaf, $i); $i++ }
        $bytes += (Get-Item $src).Length
        Move-Item -LiteralPath $src -Destination $target
        Write-Host "moved  $rel"
        $moved++
    } else {
        Write-Host "skip   $rel  (not found)"
        $skipped++
    }
}
Write-Host ""
Write-Host ("Moved {0} file(s), {1:N1} MB, into {2}" -f $moved, ($bytes/1MB), $Dest)
Write-Host ("Skipped {0}" -f $skipped)
Write-Host "Nothing was deleted. Delete _cleanup_2026-09-12 yourself once you have checked it."
