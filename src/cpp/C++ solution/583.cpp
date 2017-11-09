#include<iostream>
#include<Windows.h>
#include<tchar.h>

using namespace std;

bool isInt(long double num) {
	return (num - (int)num) == 0;
}

long double diagonal(double a, double b) {
	return sqrt(pow(a, 2) + pow(b, 2));
}

int main() {
	DWORD dwError, dwPriClass;

	if (!SetPriorityClass(GetCurrentProcess(), HIGH_PRIORITY_CLASS))
	{
		dwError = GetLastError();
		if (ERROR_PROCESS_MODE_ALREADY_BACKGROUND == dwError)
			_tprintf(TEXT("Already in background mode\n"));
		else _tprintf(TEXT("Failed to enter background mode (%d)\n"), dwError);
		return 0;
	}

	// Display priority class

	dwPriClass = GetPriorityClass(GetCurrentProcess());

	_tprintf(TEXT("Current priority class is 0x%x\n"), dwPriClass);

	const int maxP = pow(10, 7);
	int sum = 0;
	double halfBase, CD, CE, AD;
	int perimeter;
	for (int base = 1; base < maxP / 2; base++)
	{
		halfBase = base / 2.0;
		for (int side = 1; side < maxP / 2; side++)
		{
			AD = diagonal(base, side);
			if ((int)AD == side + 1) {
				break;
			}
			if (!isInt(AD)) { continue; }
			for (int flapHeight = 1; flapHeight <= side; flapHeight++)
			{
				CD = diagonal(halfBase, flapHeight);
				if (!isInt(CD)) { continue; }
				perimeter = base + side + CD + CD + side;
				if (perimeter > maxP) { break; }
				CE = diagonal(side + flapHeight, halfBase);
				if (isInt(CE)) {
					sum += perimeter;
					cout << base << ", " << side << ", " << CD << endl;
				}
			}
		}
	}
	cout << sum << endl;
	system("pause");
	return 0;
}