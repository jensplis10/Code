#include <windows.h>

int main()
{
    bool clicking = false;

    while (true)
    {

        // start clicking with `
        if (GetAsyncKeyState(VK_OEM_3) & 1)
        {
            clicking = true;
        }

        // stop clicking with ä
        if (GetAsyncKeyState(VK_OEM_7) & 1)
        {
            clicking = false;
        }

        if (clicking)
        {
            mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
            mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
        }

        // ESC closes program
        if (GetAsyncKeyState(VK_ESCAPE))
        {
            break;
        }
    }

    return 0;
}