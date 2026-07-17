# ================================================
# PowerShell HTTP Server with Arguments
# Usage: .\SimpleHttpServer.ps1 -Port 8080 -Host "127.0.0.1"
# ================================================

param(
    [int]$Port = 8080,
    [string]$HostAddr = "127.0.0.1"
)

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://$HostAddr`:$Port/")

$running = $true

Write-Host "[*] Starting HTTP Server on http://$HostAddr`:$Port" -ForegroundColor Green
Write-Host "[*] Press Ctrl+C to stop the server..." -ForegroundColor Yellow

try {
    $listener.Start()

    while ($running -and $listener.IsListening) {
        $asyncResult = $listener.BeginGetContext($null, $null)
        
        while (-not $asyncResult.IsCompleted) {
            if (-not $running) { break }
            Start-Sleep -Milliseconds 300
        }

        if (-not $running) { break }

        try {
            $context = $listener.EndGetContext($asyncResult)
            $request = $context.Request
            $response = $context.Response

            $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $remoteIP = $request.RemoteEndPoint.Address
            $rawUrl   = $request.RawUrl

            Write-Host "`n[*] [$timestamp] Request from $remoteIP" -ForegroundColor Cyan
            Write-Host "[*] Path: $rawUrl" -ForegroundColor White
            
            # Response
            $response.ContentType = "text/plain"
            $buffer = [System.Text.Encoding]::UTF8.GetBytes("OK")
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
            $response.Close()
        }
        catch { }
    }
}
catch {
    if ($_.Exception.Message -notlike "*canceled*") {
        Write-Host "[!] Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}
finally {
    Write-Host "`n[*] Stopping server..." -ForegroundColor Yellow
    if ($listener) {
        $listener.Stop()
        $listener.Close()
    }
    Write-Host "[*] Server stopped." -ForegroundColor Green
}