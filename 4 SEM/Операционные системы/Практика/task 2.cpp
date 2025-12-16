#include <windows.h>
#include <tchar.h>
#include <stdio.h>

int _tmain() {
    HANDLE hFile;
    TCHAR FileName[] = _T("MyFile.txt");
    TCHAR TextString[] = _T("Hello, world.");
    DWORD iWrite, StringLength = _tcslen(TextString);

    _tprintf(_T("There are %ld symbols in text string: %s\n"), StringLength, TextString);

    hFile = CreateFile(FileName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
        _tprintf(_T("Error creating file. Error code: %d\n"), GetLastError());
        return 1;
    }

#ifdef UNICODE
    iWrite = 2 * StringLength;
#else
    iWrite = StringLength;
#endif

    WriteFile(hFile, TextString, iWrite * sizeof(TCHAR), &iWrite, NULL);

    _tprintf(_T("%d bytes are written to the file\n"), iWrite);

    CloseHandle(hFile);

    return 0;
}