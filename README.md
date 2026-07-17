
# Chromium Lure
Generates realistic fake Windows 11 credential prompts for phishing credentials from compromised machines during authorized engagements. 

<img width="1618" height="919" alt="cred_prompt_demo" src="https://github.com/user-attachments/assets/9b2ca224-97b2-4cfc-b224-4cf45952f942" />

## Features
- Native-looking Windows 11 prompts (Light & Dark mode)
- Fully customizable message and icon
- Configurable callback URL for credential exfiltration
- optional prefilled username


For more information read the blog post: https://drewalleman.xyz/red-teaming/2026/07/16/2026-creating-fake-windows-11-credential-popups-with-google-and-edge

## Launching Chrome
Example on how to launch chrome with the generated login form:
```
$chromeArgs = @(
    '--app="C:\Users\drew\Downloads\login.html"'
    '--window-size=440,460'
    '--force-app-mode'
    '--disable-infobars'
    '--noerrdialogs'
    '--user-data-dir="C:\temp\winprompt"'
)

Start-Process -FilePath chrome.exe -ArgumentList $chromeArgs
```
## Light mode Example
Also showcasing a custom favicon and title: <br>
<img width="447" height="403" alt="image" src="https://github.com/user-attachments/assets/a0e969a6-76a3-4bd4-b184-62b3a8bb5325" />

