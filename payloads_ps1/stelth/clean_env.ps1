Clear-RecycleBin -Force
Remove-Variable * -ErrorAction SilentlyContinue
Remove-Item (Get-PSReadlineOption).HistorySavePath
exit