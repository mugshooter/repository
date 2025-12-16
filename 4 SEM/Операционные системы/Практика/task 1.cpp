#include <windows.h>
#include <tchar.h>
#include <iostream>

int _tmain() {
    HANDLE hFile;
    PTCHAR FileName = _T("MyFile.txt");
    PTCHAR TextString = _T("Hello, world.");
    DWORD iWrite, StringLength = _tcslen(TextString);
    
    _tprintf(_T("There are %ld symbols in text string %s\n"), StringLength, TextString);

    hFile = CreateFile(FileName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    
    iWrite = StringLength * sizeof(TCHAR);
    
    WriteFile(hFile, TextString, iWrite, &iWrite, NULL);
    
    _tprintf(_T("%d bytes are written to file\n"), iWrite / sizeof(TCHAR));
    
    CloseHandle(hFile);

    return 0;
}