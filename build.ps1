$exclude = @("venv", "textBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "textBot.zip" -Force