$ErrorActionPreference = 'Stop'
$taskDocPath = 'C:\Francois\Writting\HomoNoxisGithub\output\documents\Homo-Noxius-100-Question-Editorial-Questionnaire.docx'
$taskPdfPath = 'C:\Francois\Writting\HomoNoxisGithub\tmp\questionnaire-2026-11-04\render\questionnaire.pdf'
New-Item -ItemType Directory -Path (Split-Path -Parent $taskPdfPath) -Force | Out-Null
$taskWord = New-Object -ComObject Word.Application
$taskInitialDocuments = $taskWord.Documents.Count
$taskOldAlerts = $taskWord.DisplayAlerts
$taskDocument = $null
try {
    if ($taskInitialDocuments -eq 0) { $taskWord.Visible = $false }
    $taskWord.DisplayAlerts = 0
    $taskDocument = $taskWord.Documents.Open($taskDocPath, $false, $true, $false)
    $taskDocument.Repaginate()
    Write-Output "Content controls: $($taskDocument.ContentControls.Count)"
    Write-Output "Pages: $($taskDocument.ComputeStatistics(2))"
    $taskDocument.ExportAsFixedFormat($taskPdfPath, 17)
    Write-Output "Preview exported: $taskPdfPath"
} finally {
    if ($null -ne $taskDocument) { $taskDocument.Close(0) }
    $taskWord.DisplayAlerts = $taskOldAlerts
    if ($taskInitialDocuments -eq 0) { $taskWord.Quit(0) }
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($taskWord) | Out-Null
}
