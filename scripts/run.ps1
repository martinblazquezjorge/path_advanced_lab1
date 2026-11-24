$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')
$pythonPath = Join-Path (Get-Location) '.venvScriptspython.exe'
if (Test-Path -LiteralPath $pythonPath) {
    & $pythonPath -m frc_eval.cli @args
} else {
    $env:PYTHONPATH = Join-Path (Get-Location) 'src'
    python -m frc_eval.cli @args
}
exit $LASTEXITCODE
