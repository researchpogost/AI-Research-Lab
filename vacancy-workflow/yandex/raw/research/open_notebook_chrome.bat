@echo off
set "CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe"
set "USER_DATA_DIR=C:\Users\Administrator\.notebooklm-mcp\chrome-profile"

if not exist "%CHROME_PATH%" (
    echo [ERROR] Chrome not found at %CHROME_PATH%
    pause
    exit /b 1
)

echo [INFO] Launching Chrome with NotebookLM MCP profile...
start "" "%CHROME_PATH%" --user-data-dir="%USER_DATA_DIR%" --no-first-run
