Remove-Item -Path "$(Get-ChildItem -Path $env:TEMP -Recurse -Filter "window_test_pic.lock" | Select-Object -ExpandProperty FullName)"
# Removes the lock file "window_test_pic.lock"