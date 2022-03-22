$save_dir = "$HOME\Desktop\"
$img_url = "https://i.ytimg.com/vi/3tleO8QtVTE/maxresdefault.jpg"
$f = "rr.jpg" 
wget $img_url -O "$save_dir$f"
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "$save_dir$f" /f
Start-Sleep -s 3
rundll32.exe user32.dll, UpdatePerUserSystemParameters, 0, $false