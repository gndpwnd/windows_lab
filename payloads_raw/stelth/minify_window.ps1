Add-Type -Name Window -Namespace Console -MemberDefinition '
[DllImport("Kernel32.dll")] 
public static extern IntPtr GetConsoleWindow();
[DllImport("user32.dll")]
public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H); '
$consoleHWND = [Console.Window]::GetConsoleWindow();
$consoleHWND = [Console.Window]::MoveWindow($consoleHWND, 0, 0, 0, 0);
$pshost = get-host
$pswindow = $pshost.ui.rawui
$newsize = $pswindow.buffersize
$newsize.height = 2000
$newsize.width = 200
$pswindow.buffersize = $newsize
$newsize = $pswindow.windowsize
$newsize.height = 1
$newsize.width = 1
$pswindow.windowsize = $newsize