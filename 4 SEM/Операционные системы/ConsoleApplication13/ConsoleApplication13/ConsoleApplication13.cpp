#define _WIN32_WINNT 0x0500
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <stdio.h>
#include <sddl.h>

int main() {
    DWORD TokenUserBufSize = 256;
    LPTSTR StringSid;
    TOKEN_USER* ptUser;
    HANDLE hHeap;
    HANDLE hToken = NULL;

    hHeap = GetProcessHeap();
    ptUser = (TOKEN_USER*)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, TokenUserBufSize);

    if (!OpenProcessToken(GetCurrentProcess(), TOKEN_QUERY, &hToken)) {
        printf("OpenProcessToken Error\n");
        return 1;
    }

    if (!GetTokenInformation(hToken, TokenUser, ptUser, TokenUserBufSize, &TokenUserBufSize)) {
        printf("GetTokenInformation Error\n");
        CloseHandle(hToken);
        return 1;
    }

    if (!ConvertSidToStringSid(ptUser->User.Sid, &StringSid)) {
        printf("Convert SID to string SID failed.\n");
        CloseHandle(hToken);
        HeapFree(hHeap, 0, ptUser);
        return 1;
    }

    wprintf(L"StringSid %s\n", StringSid);

    CloseHandle(hToken);
    LocalFree(StringSid);
    HeapFree(hHeap, 0, ptUser);

    return 0;
}
