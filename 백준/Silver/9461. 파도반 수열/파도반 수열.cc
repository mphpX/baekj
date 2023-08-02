#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(void)
{
	int n, m;
	scanf("%d", &n);
	long long p[101];
	p[0] = 1;
	p[1] = 1;
	p[2] = 1;
	for (int i = 3;i < 101;i++) {
		p[i] = p[i - 2] + p[i - 3];
	}
	for (int i = 0;i < n;i++) {
		scanf("%d", &m);
		printf("%lld\n", p[m - 1]);
	}
	return 0;
}
