#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(void) {
	int n;
	scanf("%d", &n);
	int a = 0;
	if (n % 5 == 0) {
		a = n / 5;
		printf("%d", n / 5 );
	}
	else if (n % 5 != 0) {
		for (int p = 0; p < n / 5+1; p++) {
			if ((n - 5 * p) % 3 == 0 && p != 0) {
				a = p + (n - 5 * p) / 3;
			}
		}
		if(a!=0) printf("%d", a);
		if (a == 0 && n % 3 == 0) {
			a = n / 3;
			printf("%d", a);
		}
	}
	if (a == 0)printf("%d", -1);
	return 0;
}